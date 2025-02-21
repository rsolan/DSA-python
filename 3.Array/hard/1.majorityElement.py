https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # m1 - count in dict

        # m2 - use moore voting algo 
        # inc by 1 , dec by 1, store 2 ans
        n = len(nums)
        cnt1=0
        cnt2=0
        el1,el2 = float('inf'),float('inf')

        for i,v in enumerate(nums):
            if cnt1==0 and el2!=nums[i]:
                cnt1=1
                el1 = nums[i]
            elif cnt2==0 and el1!=nums[i]:
                cnt2=1
                el2=nums[i]
            elif nums[i] == el1:
                cnt1+=1
            elif nums[i] == el2:
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
        # check if possibel ans or not
        cnt1=0
        cnt2=0
        out=[]
        for i in nums:
            if i == el1:
                cnt1+=1
            if  cnt1> n//3:
                out.append(el1)
                break

        for i in nums:
            if i == el2:
                cnt2+=1
            if  cnt2> n//3:
                out.append(el2)
                break
            
        return out
