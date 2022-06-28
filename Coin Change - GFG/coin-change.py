#User function Template for python3

class Solution:
    def count(self, s, m, n): 
        # code here 
        t=[]
        for i in range(m+1):
            temp=[]
            for j in range(n+1):
                temp.append(0)
            t.append(temp)
        for i in range(len(t[0])):
            t[0][i] = 0
        for i in range(len(t)):
            t[i][0] = 1
       
        for i in range(m+1):
            for j in range(n+1):
                if s[i-1]<= j:
                   t[i][j] = t[i][j-s[i-1]]+t[i-1][j]
                   
                else:
                    t[i][j] = t[i-1][j]
                 
        return t[-2][-1]


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n,m = list(map(int, input().strip().split()))
        S = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(S,m,n))
# } Driver Code Ends