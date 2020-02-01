class Solution:
    def search(self, nums, target):
        def ro_idx(l, r):
            if nums[r] > nums[l]:
                return 0
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > nums[mid + 1]:
                    return mid + 1
                else:
                    if nums[mid] > nums[r]:
                        l = mid + 1
                    else:
                        r = mid
            return -1

        def bi_search(l, r, t):
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == t:
                    return mid
                if nums[mid] > t:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1

        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        r_idx = ro_idx(0, len(nums) - 1)
        if nums[r_idx] == target:
            return r_idx
        if r_idx == 0:
            return bi_search(0, len(nums) - 1, target)
        if nums[0] <= target:
            return bi_search(0, r_idx, target)
        else:
            return bi_search(r_idx, len(nums) - 1, target)


nums = [4,5,1,2,3]
target = 1
p = Solution()
a = p.search(nums,target)