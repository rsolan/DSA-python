def low_bound(self,nums: List[int], target: int ) -> int:
        # el greater than or equal to x
        n = len(nums)
        s=0
        e= n-1
        ans = n
        while s<=e:
            mid = s+(e-s)//2
            if nums[mid] >= target:
                ans = mid
                e= mid-1
            else:
                s = mid+1
        return ans

    def up_bound(self,nums: List[int], target: int ) -> int:
        # el greater than to x
        n = len(nums)
        s=0
        e= n-1
        ans = n
        while s<=e:
            mid = s+(e-s)//2
            if nums[mid] > target:
                ans = mid
                e= mid-1
            else:
                s = mid+1
        return ans
