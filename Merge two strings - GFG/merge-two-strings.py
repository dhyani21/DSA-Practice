#User function Template for python3
class Solution:
    def merge(self, S1, S2):
        res = ""
        j=0
        k=0
        for i in range(0, min(len(S1), len(S2))*2,1):
            if i%2 ==0:
                res+=S1[j]
                j+=1
            else:
                res+=S2[k]
                k+=1
        if len(S1) != len(S2):
            if min(len(S1), len(S2)) == len(S1):
                res+=S2[k:]
            else:
                res+=S1[j:]
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S1,S2 = map(str,input().strip().split())
        ob = Solution()
        print(ob.merge(S1, S2))
# } Driver Code Ends