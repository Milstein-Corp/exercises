class Solution(object):
    def match(self, w, words, rest):
        is_match = True
        for c in range(len(words[w])):
            if len(words[w]) <= len(rest) and words[w][c] == rest[c]:
                y = 2
            else:
                is_match = False
                break
        return is_match

    def wordBreak(self, s, wordDict):
        a1 = set(s)
        a2 = set()
        for w in wordDict:
            for c in w:
                a2.add(c)
        if not a1.issubset(a2):
            return False
        words = wordDict

        paths = []
        farthest = 0
        for w in range(len(words)):
            if words[w] == s[:len(words[w])]:
                paths.append([w])
                if len(words[w]) > farthest:
                    farthest = len(words[w])
        if paths:
            growing = True
        else:
            growing = False
        answer = False
        while growing:
            new_paths = []
            growing = False

            for path in paths:
                path_length = 0
                for w in path:
                    path_length += len(words[w])
                rest = s[path_length:]  # this will throw an error, if path_length too big. Shouldn't.
                if not rest:  # the path was already good.
                    new_paths.append(path)
                    answer = True
                else:
                    for w in range(len(words)):
                        new_path = list.copy(path)
                        is_match = Solution.match(Solution, w, words, rest)
                        if is_match:
                            growing = True
                            new_path.append(w)
                            new_paths.append(new_path)
            paths = new_paths

            new_paths = []
            lengths = []
            for path in paths:
                if len(path) not in lengths:
                    lengths.append(len(path))
                    new_paths.append(path)
            paths = new_paths


        return answer


if __name__ == '__main__':
    s = "penapepen"
    wordDict = ["pen", "ape"]
    actual = Solution.wordBreak(Solution, s, wordDict)
    desired = [[0, 1, 0]]
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    s = "pencilpen"
    wordDict = ["pen", "pencil", "cil"]
    actual = Solution.wordBreak(Solution, s, wordDict)
    desired = [[0, 2, 0], [1, 0]]
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    s = "pencilpen"
    wordDict = ["pen", "pencil", "cil"]
    actual = Solution.wordBreak(Solution, s, wordDict)
    desired = [[0, 2, 0], [1, 0]]
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    s = "pencilpeng"
    wordDict = ["pen", "pencil", "cil"]
    actual = Solution.wordBreak(Solution, s, wordDict)
    desired = []
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    s = "aaaaaa"
    wordDict = ["aaaa", "aa"]
    actual = Solution.wordBreak(Solution, s, wordDict)
    desired = [[0, 1], [1, 0], [1, 1, 1]]
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    s = "aaaaaaa"
    wordDict = ["aaaa", "aa"]
    actual = Solution.wordBreak(Solution, s, wordDict)
    desired = []
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    s = "ccacccbcab"
    wordDict = ["cc", "bb", "aa", "bc", "ac", "ca", "ba", "cb"]
    actual = Solution.wordBreak(Solution, s, wordDict)
    desired = []
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    s = "fohhemkkaecojceoaejkkoedkofhmohkcjmkggcmnami"
    wordDict = ["kfomka", "hecagbngambii", "anobmnikj", "c", "nnkmfelneemfgcl", "ah", "bgomgohl", "lcbjbg", "ebjfoiddndih",
     "hjknoamjbfhckb", "eioldlijmmla", "nbekmcnakif", "fgahmihodolmhbi", "gnjfe", "hk", "b", "jbfgm", "ecojceoaejkkoed",
     "cemodhmbcmgl", "j", "gdcnjj", "kolaijoicbc", "liibjjcini", "lmbenj", "eklingemgdjncaa", "m", "hkh", "fblb", "fk",
     "nnfkfanaga", "eldjml", "iejn", "gbmjfdooeeko", "jafogijka", "ngnfggojmhclkjd", "bfagnfclg", "imkeobcdidiifbm",
     "ogeo", "gicjog", "cjnibenelm", "ogoloc", "edciifkaff", "kbeeg", "nebn", "jdd", "aeojhclmdn", "dilbhl", "dkk",
     "bgmck", "ohgkefkadonafg", "labem", "fheoglj", "gkcanacfjfhogjc", "eglkcddd", "lelelihakeh", "hhjijfiodfi",
     "enehbibnhfjd", "gkm", "ggj", "ag", "hhhjogk", "lllicdhihn", "goakjjnk", "lhbn", "fhheedadamlnedh", "bin", "cl",
     "ggjljjjf", "fdcdaobhlhgj", "nijlf", "i", "gaemagobjfc", "dg", "g", "jhlelodgeekj", "hcimohlni", "fdoiohikhacgb",
     "k", "doiaigclm", "bdfaoncbhfkdbjd", "f", "jaikbciac", "cjgadmfoodmba", "molokllh", "gfkngeebnggo", "lahd", "n",
     "ehfngoc", "lejfcee", "kofhmoh", "cgda", "de", "kljnicikjeh", "edomdbibhif", "jehdkgmmofihdi", "hifcjkloebel",
     "gcghgbemjege", "kobhhefbbb", "aaikgaolhllhlm", "akg", "kmmikgkhnn", "dnamfhaf", "mjhj", "ifadcgmgjaa",
     "acnjehgkflgkd", "bjj", "maihjn", "ojakklhl", "ign", "jhd", "kndkhbebgh", "amljjfeahcdlfdg", "fnboolobch",
     "gcclgcoaojc", "kfokbbkllmcd", "fec", "dljma", "noa", "cfjie", "fohhemkka", "bfaldajf", "nbk", "kmbnjoalnhki",
     "ccieabbnlhbjmj", "nmacelialookal", "hdlefnbmgklo", "bfbblofk", "doohocnadd", "klmed", "e", "hkkcmbljlojkghm",
     "jjiadlgf", "ogadjhambjikce", "bglghjndlk", "gackokkbhj", "oofohdogb", "leiolllnjj", "edekdnibja", "gjhglilocif",
     "ccfnfjalchc", "gl", "ihee", "cfgccdmecem", "mdmcdgjelhgk", "laboglchdhbk", "ajmiim", "cebhalkngloae",
     "hgohednmkahdi", "ddiecjnkmgbbei", "ajaengmcdlbk", "kgg", "ndchkjdn", "heklaamafiomea", "ehg", "imelcifnhkae",
     "hcgadilb", "elndjcodnhcc", "nkjd", "gjnfkogkjeobo", "eolega", "lm", "jddfkfbbbhia", "cddmfeckheeo", "bfnmaalmjdb",
     "fbcg", "ko", "mojfj", "kk", "bbljjnnikdhg", "l", "calbc", "mkekn", "ejlhdk", "hkebdiebecf", "emhelbbda", "mlba",
     "ckjmih", "odfacclfl", "lgfjjbgookmnoe", "begnkogf", "gakojeblk", "bfflcmdko", "cfdclljcg", "ho", "fo", "acmi",
     "oemknmffgcio", "mlkhk", "kfhkndmdojhidg", "ckfcibmnikn", "dgoecamdliaeeoa", "ocealkbbec", "kbmmihb", "ncikad",
     "hi", "nccjbnldneijc", "hgiccigeehmdl", "dlfmjhmioa", "kmff", "gfhkd", "okiamg", "ekdbamm", "fc", "neg", "cfmo",
     "ccgahikbbl", "khhoc", "elbg", "cbghbacjbfm", "jkagbmfgemjfg", "ijceidhhajmja", "imibemhdg", "ja", "idkfd",
     "ndogdkjjkf", "fhic", "ooajkki", "fdnjhh", "ba", "jdlnidngkfffbmi", "jddjfnnjoidcnm", "kghljjikbacd", "idllbbn",
     "d", "mgkajbnjedeiee", "fbllleanknmoomb", "lom", "kofjmmjm", "mcdlbglonin", "gcnboanh", "fggii", "fdkbmic",
     "bbiln", "cdjcjhonjgiagkb", "kooenbeoongcle", "cecnlfbaanckdkj", "fejlmog", "fanekdneoaammb", "maojbcegdamn",
     "bcmanmjdeabdo", "amloj", "adgoej", "jh", "fhf", "cogdljlgek", "o", "joeiajlioggj", "oncal", "lbgg", "elainnbffk",
     "hbdi", "femcanllndoh", "ke", "hmib", "nagfahhljh", "ibifdlfeechcbal", "knec", "oegfcghlgalcnno", "abiefmjldmln",
     "mlfglgni", "jkofhjeb", "ifjbneblfldjel", "nahhcimkjhjgb", "cdgkbn", "nnklfbeecgedie", "gmllmjbodhgllc",
     "hogollongjo", "fmoinacebll", "fkngbganmh", "jgdblmhlmfij", "fkkdjknahamcfb", "aieakdokibj", "hddlcdiailhd",
     "iajhmg", "jenocgo", "embdib", "dghbmljjogka", "bahcggjgmlf", "fb", "jldkcfom", "mfi", "kdkke", "odhbl", "jin",
     "kcjmkggcmnami", "kofig", "bid", "ohnohi", "fcbojdgoaoa", "dj", "ifkbmbod", "dhdedohlghk", "nmkeakohicfdjf",
     "ahbifnnoaldgbj", "egldeibiinoac", "iehfhjjjmil", "bmeimi", "ombngooicknel", "lfdkngobmik", "ifjcjkfnmgjcnmi",
     "fmf", "aoeaa", "an", "ffgddcjblehhggo", "hijfdcchdilcl", "hacbaamkhblnkk", "najefebghcbkjfl", "hcnnlogjfmmjcma",
     "njgcogemlnohl", "ihejh", "ej", "ofn", "ggcklj", "omah", "hg", "obk", "giig", "cklna", "lihaiollfnem",
     "ionlnlhjckf", "cfdlijnmgjoebl", "dloehimen", "acggkacahfhkdne", "iecd", "gn", "odgbnalk", "ahfhcd", "dghlag",
     "bchfe", "dldblmnbifnmlo", "cffhbijal", "dbddifnojfibha", "mhh", "cjjol", "fed", "bhcnf", "ciiibbedklnnk",
     "ikniooicmm", "ejf", "ammeennkcdgbjco", "jmhmd", "cek", "bjbhcmda", "kfjmhbf", "chjmmnea", "ifccifn", "naedmco",
     "iohchafbega", "kjejfhbco", "anlhhhhg"]

    print(len(wordDict))

    s = set(wordDict)
    print(len(s))

