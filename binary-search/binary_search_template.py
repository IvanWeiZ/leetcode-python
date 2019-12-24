class BinarySearch:
    def search(self, nums, target):
        if not nums:
            return -1

        start = 0
        end = len(nums)-1

        while start + 1 < end:
            mid = start + (end - start)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

if __name__ == "__main__":
    bs = BinarySearch()
    print(bs.search([3,1,5,7,8,9], 5))
