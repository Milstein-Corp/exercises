class Solution(object):
    def findRadius(self, A, B):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        radius = 0
        for a in range(len(A)):
            r = 0
            while A[a] > B[r]:
                r += 1
                if r == len(B):
                    break
            print(str(r) + ", ", end='')
            # for this a, r is the right heater.
            # 0 <= r <= len(B)
            # r - 1 is the left heater, unless the r heater is the furthest left

            if r == 0:
                newradius = B[r] - A[a]
            elif r == len(B):
                newradius = A[a] - B[r-1]
            else:
                dist_right = B[r] - A[a]
                dist_left = A[a] - B[r-1]
                if dist_left < dist_right:
                    newradius = dist_left
                else:
                    newradius = dist_right

            if newradius > radius:
                radius = newradius

        return radius

def main():
    A = [1, 2, 3, 4]
    B = [1, 4]
    print(A)
    print(B)
    r = Solution.findRadius(Solution, A, B)
    print("required radius: %s" % str(r))
    print("\n")

    A = [1, 2, 3, 4]
    B = [1, 2]
    print(A)
    print(B)
    r = Solution.findRadius(Solution, A, B)
    print("required radius: %s" % str(r))
    print("\n")

    A = [1, 2, 3, 4]
    B = [1, 2, 3]
    print(A)
    print(B)
    r = Solution.findRadius(Solution, A, B)
    print("required radius: %s" % str(r))
    print("\n")

    A = [1, 2, 3, 4]
    B = [1, 2, 3, 4]
    print(A)
    print(B)
    r = Solution.findRadius(Solution, A, B)
    print("required radius: %s" % str(r))
    print("\n")

    A = [1, 3]
    B = [1, 2, 3, 4]
    print(A)
    print(B)
    r = Solution.findRadius(Solution, A, B)
    print("required radius: %s" % str(r))
    print("\n")

    A = [1, 2, 3, 4]
    B = [1]
    print(A)
    print(B)
    r = Solution.findRadius(Solution, A, B)
    print("required radius: %s" % str(r))
    print("\n")

    A = []
    B = [1, 2, 3, 4]
    print(A)
    print(B)
    r = Solution.findRadius(Solution, A, B)
    print("required radius: %s" % str(r))
    print("\n")

    A = [1, 2, 3, 4]
    B = [1, 4]
    print(A)
    print(B)
    r = Solution.findRadius(Solution, A, B)
    print("required radius: %s" % str(r))
    print("\n")

    A = [1, 5]
    B = [10]
    print(A)
    print(B)
    r = Solution.findRadius(Solution, A, B)
    print("required radius: %s" % str(r))
    print("\n")

    A = [282475249, 622650073, 984943658, 144108930, 470211272, 101027544, 457850878, 458777923]
    B = [823564440, 115438165, 784484492, 74243042, 114807987, 137522503, 441282327, 16531729, 823378840, 143542612]
    print(A)
    print(B)
    r = Solution.findRadius(Solution, A, B)
    print("required radius: %s" % str(r))
    print("\n")


if __name__ == '__main__':
    main()




