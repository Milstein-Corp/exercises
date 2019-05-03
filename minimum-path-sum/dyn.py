class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        a = nums[0]
        b = nums[1]
        c = nums[2] + nums[0]

        for i in range(len(nums) - 3):
            k = i + 3
            best = nums[k] + max(a, b)
            a = b
            b = c
            c = best
            # c now holds the best value for index k
            # b holds the best value for k-1
            # a holds the best value for k-2

        return max(c, b)

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        columns = len(grid[0])

        ids = []

        for r in range(rows):
            ids.append([None] * columns)

        r = 0
        c = 0
        ids[0][0] = grid[0][0]

        r = 0
        for c in range(columns)[1:]:
            ids[r][c] = grid[r][c] + ids[r][c - 1]

        c = 0
        for r in range(rows)[1:]:
            ids[r][c] = grid[r][c] + ids[r - 1][c]

        for r in range(rows)[1:]:
            for c in range(columns)[1:]:
                ids[r][c] = min(ids[r - 1][c], ids[r][c - 1]) + grid[r][c]

        print("\nprinting the intermediate data structure\n")
        for r in range(rows):
            for c in range(columns):
                print(ids[r][c], end=', ')
            print()

        print()
        return ids[-1][-1]


def main():
    input = [[1, 3, 1],
             [1, 5, 1],
             [4, 2, 1]]
    output = 7
    a = Solution.minPathSum(Solution, input)
    print("desired output: %d" % output)
    print("actual output: %d" % a)
    print()


if __name__ == '__main__':
    main()
