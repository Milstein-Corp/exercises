from datetime import time as t

LAST = 1439


def makeBitmap(c1, c2, start, finish):
    # start is the first minute available for meeting
    # finish is the last minute available for meeting

    # pre-process "start" and "finish"
    start_p = start.hour * 60 + start.minute
    finish_p = finish.hour * 60 + finish.minute

    # pre-process schedules
    c1_p = []
    for meeting in c1:
        meeting_p = (meeting[0].hour * 60 + meeting[0].minute, meeting[1].hour * 60 + meeting[1].minute)
        c1_p.append(meeting_p)

    c2_p = []
    for meeting in c2:
        meeting_p = (meeting[0].hour * 60 + meeting[0].minute, meeting[1].hour * 60 + meeting[1].minute)
        c2_p.append(meeting_p)

    # build bitmap
    day = [True] * (LAST + 1)

    # block-out times for person 1
    for meeting in c1_p:
        for m in range(meeting[0], meeting[1] + 1):
            day[m] = False

    # block-out times for person 2
    for meeting in c2_p:
        for m in range(meeting[0], meeting[1] + 1):
            day[m] = False

    # block out times before start
    for m in range(0, start_p):
        day[m] = False

    # block out times after finish
    for m in range(finish_p + 1, LAST + 1):
        day[m] = False

    return day


def produceSchedule(bm, duration):
    avails = []
    count = 0
    meeting = False
    meeting_start = -1
    for m in range(len(bm)):
        if bm[m] and not meeting:  # start of meeting
            count = 1
            meeting = True
            meeting_start = m
        elif bm[m] and meeting:  # middle of ongoing meeting
            count += 1
            meeting = True
        elif not bm[m] and meeting:  # end of meeting
            valid_meeting = (meeting_start, m - 1)
            meeting = False
            if count >= duration:
                avails.append(valid_meeting)
        elif not bm[m] and not meeting:  # no possible meeting
            pass

    if bm[-1]:  # edge case where meeting goes to the last minute of the day
        valid_meeting = (meeting_start, len(bm) - 1)
        if count >= duration:
            avails.append(valid_meeting)

    return avails


def formatSchedule(meetings):
    """
    Reformat the way that a "time" is reported
    :param avails: list of tuples. Each tuple is an available meeting.
    :return c: list of tuples. Each tuple is an available meeting. The times are
    now reported as a datetime.time object, rather than a minute.
    """
    formatted_meetings = []

    for meeting in meetings:
        formatted_meetings.append(
            (t(meeting[0]//60, meeting[0]%60), t(meeting[1]//60, meeting[1]%60))
        )

    return formatted_meetings


def findAvailable(c1, c2, start, finish, duration):
    bm = makeBitmap(c1, c2, start, finish)
    schedule = produceSchedule(bm, duration)
    schedule_f = formatSchedule(schedule)
    return schedule_f


if __name__ == '__main__':
    # ************** findAvailable() Testing *****************

    print("findAvailable(..) Testing")
    print()
    # !!!!!!!!!!!!!!!!!!!!!!! MOST IMPORTANT TEST !!!!!!!!!!!!!!!!!!!!!!!!
    # only the final hour in the day is available, because of a combination of
    # person 1, person 2, and start restrictions
    c1 = [(t(5, 0), t(10, 59))]
    c2 = [(t(11, 0), t(22, 59))]
    start = t(5, 0)
    finish = t(23, 59)
    duration = 1
    desired = [(t(23, 0), t(23, 59))]
    actual = findAvailable(c1, c2, start, finish, duration)
    print("Only the final hour is available")
    print("desired output: %s " % desired)
    print("actual output : % s " % actual)
    print()
    assert desired == actual

    # !!!!!!!!!!!!!!!!!!!!!!! MOST IMPORTANT TEST !!!!!!!!!!!!!!!!!!!!!!!!
    # only the first hour in the day is available, because of a combination of
    # person 1, person 2, and finish restrictions
    c1 = [(t(1, 0), t(10, 59))]
    c2 = [(t(11, 0), t(11, 59))]
    start = t(0, 0)
    finish = t(11, 59)
    duration = 1
    desired = [(t(0, 0), t(0, 59))]
    actual = findAvailable(c1, c2, start, finish, duration)
    print("Only the first hour is available")
    print("desired output: %s " % desired)
    print("actual output : % s " % actual)
    print()
    assert desired == actual

    # !!!!!!!!!!!!!!!!!!!!!!! MOST IMPORTANT TEST !!!!!!!!!!!!!!!!!!!!!!!!
    # only the lunch hour in the day is available, because of a combination of
    # person 1, person 2, start, and finish restrictions
    c1 = [(t(5, 0), t(10, 59))]
    c2 = [(t(11, 0), t(11, 59))]
    start = t(5, 0)
    finish = t(12, 59)
    duration = 1
    desired = [(t(12, 00), t(12, 59))]
    actual = findAvailable(c1, c2, start, finish, duration)
    print("Only the lunch hour is available")
    print("desired output: %s " % desired)
    print("actual output : % s " % actual)
    print()
    assert desired == actual

    # the whole day is available
    c1 = []
    c2 = []
    start = t(0, 00)
    finish = t(23, 59)
    duration = 30
    desired = [(t(0, 0), t(23, 59))]
    actual = findAvailable(c1, c2, start, finish, duration)
    assert desired == actual

    # none of the day is available because of 'start' and 'finish' restriction.
    # 'start' comes after 'finish'
    c1 = []
    c2 = []
    start = t(23, 59)
    finish = t(0, 59)
    duration = 30
    desired = []
    actual = findAvailable(c1, c2, start, finish, duration)
    assert desired == actual

    # none of the day is available because of person 1
    c1 = [(t(0, 0), t(23, 59))]
    c2 = []
    start = t(0, 00)
    finish = t(23, 59)
    duration = 30
    desired = []
    actual = findAvailable(c1, c2, start, finish, duration)
    assert desired == actual

    # the first 120 min of the day are not available
    c1 = [(t(0, 00), t(0, 59))]
    c2 = [(t(1, 00), t(1, 59))]
    start = t(0, 00)
    finish = t(23, 59)
    duration = 30
    desired = [(t(2, 0), t(23, 59))]
    actual = findAvailable(c1, c2, start, finish, duration)
    assert desired == actual
    print()
    # ************** formatSchedule() Testing *****************

    times = [(1, 2), (4, 5)]
    desired = [(t(0, 1), t(0, 2)), (t(0, 4), t(0, 5))]
    actual = formatSchedule(times)
    assert actual == desired

    times = [(60, 119), (900, 1019)]
    desired = [(t(1, 0), t(1, 59)), (t(15, 0), t(16, 59))]
    actual = formatSchedule(times)
    assert actual == desired

    # ************** produceSchedule() Testing *****************

    # 1 available block, not at start or finish
    bm = [False, True, True, False]
    duration = 1
    actual = produceSchedule(bm, duration)
    desired = [(1, 2)]
    assert desired == actual

    # 1 available block, at finish
    bm = [False, False, True, True]
    duration = 1
    actual = produceSchedule(bm, duration)
    desired = [(2, 3)]
    assert desired == actual

    # 1 available block, at start
    bm = [True, True, False, False]
    duration = 1
    actual = produceSchedule(bm, duration)
    desired = [(0, 1)]
    assert desired == actual

    # 1 available block, not at start or finish, but smaller than duration
    bm = [False, True, True, False]
    duration = 3
    actual = produceSchedule(bm, duration)
    desired = []
    assert desired == actual

    # 1 available block, at finish, but smaller than duration
    bm = [False, False, True, True]
    duration = 3
    actual = produceSchedule(bm, duration)
    desired = []
    assert desired == actual

    # 1 available block, at start, but smaller than duration
    bm = [True, True, False, False]
    duration = 3
    actual = produceSchedule(bm, duration)
    desired = []
    assert desired == actual

    # 2 available blocks, not at start or finish, same length as duration
    bm = [False, True, True, False, True, True, False]
    duration = 2
    actual = produceSchedule(bm, duration)
    desired = [(1, 2), (4, 5)]
    assert desired == actual

    # 2 available blocks, one at finish, both longer than duration
    bm = [False, True, True, False, True, True, True]
    duration = 1
    actual = produceSchedule(bm, duration)
    desired = [(1, 2), (4, 6)]
    assert desired == actual

    # 2 available blocks, one at finish, one longer than duration, one the same length
    bm = [False, True, True, False, True, True, True]
    duration = 2
    actual = produceSchedule(bm, duration)
    desired = [(1, 2), (4, 6)]
    assert desired == actual

    # 2 available blocks, one sufficiently long, but one too short
    bm = [False, True, True, False, True, True, True]
    duration = 3
    actual = produceSchedule(bm, duration)
    desired = [(4, 6)]
    assert desired == actual

    # 2 available blocks, both are too short
    bm = [False, True, True, False, True, True, True]
    duration = 4
    actual = produceSchedule(bm, duration)
    desired = []
    assert desired == actual

    # 1 giant block, sufficiently long, reaches the end, not at start
    bm = [False, True, True, True, True, True, True]
    duration = 2
    actual = produceSchedule(bm, duration)
    desired = [(1, 6)]
    assert desired == actual

    # 1 giant block, but not sufficiently long, not from the start
    bm = [False, True, True, True, True, True, True]
    duration = 19
    actual = produceSchedule(bm, duration)
    desired = []
    assert desired == actual

    # 1 giant block, but not sufficiently long. Includes the start minute and final minute
    bm = [True, True, True, True, True, True, True]
    duration = 19
    actual = produceSchedule(bm, duration)
    desired = []
    assert desired == actual

    # 1 giant block, sufficiently long. Includes the start minute and final minute
    bm = [True, True, True, True, True, True, True]
    duration = 4
    actual = produceSchedule(bm, duration)
    desired = [(0, 6)]
    assert desired == actual

    # ************** makeBitmap() Testing *****************

    # the first 60 min of the day are not available

    c2 = [(t(0, 00), t(0, 59))]
    start = t(0, 00)
    finish = t(23, 59)
    duration = 30
    desired_bitmap = [True] * (LAST + 1)
    for m in range(0, 60):
        desired_bitmap[m] = False
    actual = makeBitmap(c1, c2, start, finish)
    assert desired_bitmap == actual

    # the first 120 min of the day are not available
    c1 = [(t(0, 00), t(0, 59))]
    c2 = [(t(1, 00), t(1, 59))]
    start = t(0, 00)
    finish = t(23, 59)
    duration = 30
    desired_bitmap = [True] * (LAST + 1)
    for m in range(0, 120):
        desired_bitmap[m] = False
    actual = makeBitmap(c1, c2, start, finish)
    assert desired_bitmap == actual

    # the first 120 min of the day are not available, due to start time restrictions and schedules
    c1 = [(t(0, 00), t(0, 59))]
    c2 = [(t(1, 00), t(1, 59))]
    start = t(2, 00)
    finish = t(23, 59)
    duration = 30
    desired_bitmap = [True] * (LAST + 1)
    for m in range(0, 120):
        desired_bitmap[m] = False
    actual = makeBitmap(c1, c2, start, finish)
    assert desired_bitmap == actual

    # the first 120 min of the day are not available, due only to start time restrictions
    c1 = []
    c2 = []
    start = t(2, 00)
    finish = t(23, 59)
    duration = 30
    desired_bitmap = [True] * (LAST + 1)
    for m in range(0, 120):
        desired_bitmap[m] = False
    actual = makeBitmap(c1, c2, start, finish)
    assert desired_bitmap == actual

    # The entire day is available
    c1 = []
    c2 = []
    start = t(0, 00)
    finish = t(23, 59)
    duration = 30
    desired_bitmap = [True] * (LAST + 1)
    for m in range(0, 0):
        desired_bitmap[m] = False
    actual = makeBitmap(c1, c2, start, finish)
    assert desired_bitmap == actual
