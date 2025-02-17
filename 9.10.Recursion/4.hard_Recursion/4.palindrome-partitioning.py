https://leetcode.com/problems/palindrome-partitioning/


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        move the partition at all index
        check if left string is pal so continue , otherwise return false

        test case
        aabb
        a abb                 || aa bb      || aab b            || aabb   -> stop i crosses n-1 
        abb-a,ab,abb            bb- b,bb
        only a is possible

        a,a| bb                aa,b|b : aa,bb|         x aab not pal        x
        bb- b,bb
        

        a,a,b|b  :a,a,bb|       aa,b,b|: stop
        a,a,b,b|  :stop          stop
        stop

        a,a,b,b   a,a,bb        aa,b,b  aa,bb  -> ans

        base case if i reaches n - return ans
        '''

        def check_pal(s,ind,i):
            # check if str is pal from ind to ith index
            start = ind
            end = i
            while start<=end:
                if s[start]!=s[end]:
                    return False
                start+=1
                end-=1
            return True
            

        def rec(ind,s,ds,out):
            if ind ==n:
                out.append(ds[:])
                return

            for i in range(ind,n):  #aa bb  , ind = 1
                if check_pal(s,ind,i): #chech if aa is pal     ;check if a,aa,aab,aabb is pal
                    ds.append(s[ind:i+1])   #include i so  0and1 so ds=[aa,]
                    rec(i+1,s,ds,out)
                    ds.pop()

            
        n = len(s)
        out =[]
        ds=[]
        rec(0,s,ds,out)
        return out


