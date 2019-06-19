# Definition for singly-linked list.

class Solution(object):
    def numUniqueEmails(self, emails):
        if len(emails) == 0:
            return 0
        emails = [i.split("@") for i in emails]

        for e in emails:
            e[0] = e[0].replace(".", "")
            try:
                ind = e[0].index("+")
                e[0] = e[0][:ind]
            except ValueError:
                pass
        emails = sorted([e[0] + e[1] for e in emails])
        p = e[0] + "8"
        count = 0
        for e in emails:
            if e != p:
                count += 1
            p = e
        return count



if __name__ == '__main__':
    emails = ["my@gmail.com", "my+you@yahoo.com", "m.y@gmail.com", "m.y@yahoo.com"]
    actual = Solution.numUniqueEmails(Solution, emails)
    assert actual == 2
    print("actual: " + str(actual))
    print()

    emails = [".my@gmail.com", "my+you@yahoo.com", "m.y@gmail.com", "m.y@yahoo.com"]
    actual = Solution.numUniqueEmails(Solution, emails)
    assert actual == 2
    print("actual: " + str(actual))
    print()

    emails = ["my@gmail.com", "my+you@yahoo.com", "my@gmail.com", "m.y@yahoo.com"]
    actual = Solution.numUniqueEmails(Solution, emails)
    assert actual == 2
    print("actual: " + str(actual))
    print()

    emails = ["my+@gmail.com", "my+you@yahoo.com", "my@gmail.com", "m.y@yahoo.com"]
    actual = Solution.numUniqueEmails(Solution, emails)
    assert actual == 2
    print("actual: " + str(actual))
    print()

    emails = ["m.y+steve@gmail.com", "my+you@yahoo.com", "my@gmail.com", "m.y@yahoo.com"]
    actual = Solution.numUniqueEmails(Solution, emails)
    assert actual == 2
    print("actual: " + str(actual))
    print()
