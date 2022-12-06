#User function Template for python3

class Solution:
    def factorialNumbers(self, N):
    	#code here 
    	def solve(f,x,a):
    	    if(f>N):
    	        return
    	    a.append(f)
    	    solve(f*x,x+1,a)
    	    
    	a = []
    	solve(1,2,a)
    	return a


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ")
        print()
        
# } Driver Code Ends