#User function Template for python3


class Solution:
    def MissingNumber(self,array,n):
        x  = [l for l in range(1,n+1)]
        y = set(x)
        z = set(array)
        b = list(y.difference(z))
        return b[0]

#{ 
#  Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends