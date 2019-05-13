from operator import itemgetter, attrgetter

if __name__ == '__main__':
    print("************************Sort a Dictionary*****************************")
    b = {4: 'a', 3: 'b', 2: 'c', 1: 'd'}
    print("PRINT A DICTIONARY by using items method")
    print("dict items: ", end='')
    print(b.items())
    print("type: %s" % type(b.items()))
    # it seems like a dict_items object is essentially a list.
    for k, v in b.items():
        print("key: %s, value: %s" % (k, v))
    print()
    print("SORT THE DICTIONARY KEYS, PUT IN LIST")
    c = sorted(b)
    print(c)
    for k in c:
        print("key: %s, value: %s" % (k, b[k]))
    print()
    print("SORT THE DICTIONARY ITEMS object")
    print("DICT ITEMS IS PRETTY MUCH A LIST OF TUPLES")
    items = b.items()
    sorteditems = sorted(items)
    print("Unsorted ITEMS: %s " % items)
    print("SORTED ITEMS: %s " % sorteditems)
    print("type: sorteditems: %s " % type(sorteditems))
    print("when I sort the dictionary items object, i get back a list" \
          " of tuples sorted by 'key' (the first element)")
    print()

    print("******************************Sorting Tuples***********************")
    objects = [('hammer', 3), ('pencil', .1), ('car', 2000), ('book', 5)]
    sortedobjects = sorted(objects)
    sortedWeight = sorted(objects, key=lambda x: x[1])
    print("unsorted: %s" % objects)
    print("sorted alphabetically: %s " % sortedobjects)
    print("sorted by weight: %s " % sortedWeight)
    print()
    points = [(5, .2), (.5, 2), (1, 1), (2, .5), (3, .33), (4, .25)]
    x = sorted(points)
    reciprocal = sorted(points, key=lambda x: x[1])
    print("unsorted: %s " % points)
    print("sorted by point: %s " % x)
    print("sorted by reciprocal: %s " % reciprocal)
    print()

    game = [(5, 1, 1, 1), (2, 2, 2, 3), (7, 0, 0, 0), (4, 1, 1, 1), (3, 1, 1, 1), (2, 1, 1, 1)]
    print("unsorted: %s " % game)
    print("first quarter: % s" % sorted(game, key = lambda x: -x[0]))
    print("first quarter: % s" % sorted(game, key = lambda x: x[0], reverse=True))
    print("all game: % s" % sorted(game, key=lambda x: x[0]+x[1]+x[2]+x[3], reverse=True))
    print("first, second, third: % s" % sorted(game, key=itemgetter(0, 1, 2), reverse=True))

    print("******************************Sorting Custom built objects***********************")
    class company:
        def __init__(self, position, salary, company):
            self.position = position
            self.salary = salary
            self.company = company

    a = company("devops", 100, "apple")
    b = company("ml", 200, "google")
    c = company("sre", 40, "zymergen")
    d = company("frontend", 40, "disney")

    options = [b, a, c, d]
    print("Companies Alphabetically:")
    for o in sorted(options, key=lambda x: x.company):
        print(o.company)
    print("Companies, By Salary")
    for o in sorted(options, key=lambda x: x.salary):
        print(o.company)
    print("Companies, By Salary, then alphabetically")
    for o in sorted(options, key=attrgetter('salary', 'company')):
        print(o.company)


