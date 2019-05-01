class Solution(object):
    def findRadius(self, A, B):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        radius = 1
        for a in range(len(A)):
            r = 0
            while A[a] > B[r]:
                r += 1
                if r == len(B):
                    break
            print(str(r) + ", ", end='')

        print()

def main():
    A = [1, 2, 3, 4]
    B = [1, 4]
    print(A)
    print(B)
    Solution.findRadius(Solution, A, B)
    print("0, 1, 1, 1, = should be")
    print("\n\n\n")

    A = [1, 2, 3, 4]
    B = [1, 2]
    print(A)
    print(B)
    Solution.findRadius(Solution, A, B)
    print("0, 1, 2, 2, = should be")
    print("\n\n\n")

    A = [1, 2, 3, 4]
    B = [1, 2, 3]
    print(A)
    print(B)
    Solution.findRadius(Solution, A, B)
    print("0, 1, 2, 3, = should be")


if __name__ == '__main__':
    main()




