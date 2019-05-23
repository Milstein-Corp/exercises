import heapq

class Kthlargest(object):

    def __init__(self, k, nums):
        self.heap = nums
        heapq.heapify(self.heap)
        self.k = k

    def add(self, val):
        heapq.heappush(self.heap, val)


        holder = []
        for i in range(1, self.k):
            ans = heapq.heappop(self.heap)
            holder.append(ans)
        ans = heapq.heappop(self.heap)

        for p in holder:
            heapq.heappush(self.heap, p)

        return ans


class KthLargest(object):
    import heapq

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        nums.sort()
        self.heap = nums[-k:]
        self.k = k
        heapq.heapify(self.heap)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val >= self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        return self.heap[0]


if __name__ == '__main__':
    r = [0, 1, 2, 3, 4, 5, 6, 99]
    camel = Kthlargest(2, r)
    actual = camel.add(0)
    desired = 0
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    r = [0, 1, 2, 3, 4, 5, 6, 99]
    camel = Kthlargest(2, r)
    actual = camel.add(99)
    desired = 1
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    r = [0, 1, 2, 3, 4, 5, 6, 99]
    k = 3
    camel = Kthlargest(k, r)
    actual = camel.add(99)
    desired = 2
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    r = [0, 1, 2, 3, 4, 5, 6, 99]
    k = 3
    camel = Kthlargest(k, list.copy(r))
    actual = camel.add(0)
    desired = 1
    print("array: %s" % r)
    print("k: %s " % k)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    r = [0, 0, 2, 3, 4, 5, 6, 99]
    k = 3
    camel = Kthlargest(k, list.copy(r))
    actual = camel.add(99)
    desired = 2
    print("array: %s" % r)
    print("k: %s " % k)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()
