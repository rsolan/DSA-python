https://leetcode.com/problems/hand-of-straights/


class Solution:
    def isNStraightHand(self, hand: List[int], k: int) -> bool:
        if len(hand) % k != 0:  # First check if it is divisible by k
            return False
        d={}
        for i in hand:
            if i in d:
                d[i]+=1
            else:
                d[i]=1

        n = len(hand)
        hand.sort()

        print(d)
        print(hand) 

        for card in hand:
            if d[card] == 0:
                continue
            for j in range(k): # 0 1 2  -> 1 2 3
                # print(card+j)
                # print(d[card + j])
                if card+j in d and d[card+j] >0:  #-- check this condition --IMP TO CHECK >0 as it can be neg , we cant deleet also as we have to continue in case of 0 freq
                    d[card+j]-=1
                else:
                    return False
            # print(card,j,d)

        return True




        
        #  cons 3 el
        #  3 groups - x
        # group al el -- each has to be of groupsize 3


        # len = mult of 4

        # [1,2,3,6,2,3,4,7,8]

        # minheap 
        # pop the min el 
        # - maintain 3 size  1 2 4 3 -- check cons nature
        # vis - 1 2 
        # pop 2 and pushit back in next itr

''' - nowt workng
        n = len(hand)

        vis = [0]*n
        for i in range(n):
            if vis[i]==0:
                vis[i]=1
                cnt =1
                for j in range(i+1,n):
                    if hand[j] ==hand[i]+1:
                        vis[j] =1
                        cnt+=1

                    if hand[j] == hand[i]+2:
                        vis[j]=1
                        cnt+=1

                if cnt!=3:
                    return False
            else:
                continue

        return True
        '''
