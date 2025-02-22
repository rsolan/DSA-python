https://leetcode.com/problems/maximize-the-confusion-of-an-exam/description/

class Solution:
    def maxConsecutiveAnswers(self, a: str, k: int) -> int:

        def fun(p):
            r = 0
            l = 0
            n = len(a)
            cnt = 0

            maxi  = 0

            for r in range(n):
                if a[r]==p:
                    cnt+=1
                
                if cnt>k:
                    if a[l] == p:
                        cnt-=1
                    l+=1
                maxi = max(maxi,r-l+1)

            return maxi




        ans1 = fun('T')
        ans2 = fun('F')

        return max(ans1,ans2)


        '''
        # solve it urself usuing p 
        def slide(answerKey,left):
            while f>k:
                if answerKey[left] == 'F':
                    f-=1
                else:
                    t-=1
                left+=1
            return left

        n = len(answerKey)
        left = 0
        f=0
        t =0
        maxi1=0
        maxi2=0
        for right in range(n):
            if answerKey[right] == 'F':
                f+=1
            else:
                t+=1

            if f>k:
                compressionLogic()

            maxi1 = max(maxi1,right-left+1)

        # m2 
        # n = len(answerKey)
        # left = 0
        # f=0
        # t =0
        # maxi1=0
        # maxi2=0
        # for right in range(n):
        #     if answerKey[right] == 'F':
        #         f+=1
        #     else:
        #         t+=1

        #     while f>k:
        #         if answerKey[left] == 'F':
        #             f-=1
        #         else:
        #             t-=1
        #         left+=1

        #     maxi1 = max(maxi1,right-left+1)

        # # use second loop as win len will change
        # left = 0
        # f=0
        # t =0
        # for right in range(n):
        #     if answerKey[right] == 'F':
        #         f+=1
        #     else:
        #         t+=1

        #     while t>k:
        #         if answerKey[left] == 'F':
        #             f-=1
        #         else:
        #             t-=1
        #         left+=1

        #     maxi2 = max(maxi2,right-left+1) 

        # return max(maxi1,maxi2)

        '''
