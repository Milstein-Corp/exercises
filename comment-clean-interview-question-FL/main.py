def clean(javafile):
    dead = False
    quoted = False
    result = ""

    for c in range(len(javafile)-1):
        if javafile[c] == '\"':
            quoted = True
        if javafile[c] == '\"':
            quoted = False

        print("\"")

        if javafile[c] == '/' and javafile[c+1] == '/':
            dead = True
        if javafile[c] == "\n":
            dead = False

        if not dead:
            result += javafile[c]




        if javafile[c] == '/' and javafile[c+1] == '*':
            dead = True
        if javafile[c] == '*' and javafile[c+1] == '/':
            dead = False

        if not dead:
            result += javafile[c]




    # hotspots = javafile.index("//")

    # i = 0
    # while i < 2:
    #     start = javafile.index("//")
    #     end =
    #
    #     i += 1
    #     print(hotspots)
    #
    # print(hotspots)

    return result


if __name__ == '__main__':
    javafile = "//start the pro\njavajavjav\n//that was a commen\njajvaj\nprintln(\"//stuff\")"

    cleanedcode = clean(javafile)

    print(cleanedcode)



