class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	b =[]
    	A = []
    	for i in range(n):
    	    A.append(0)
    	 
    	for i in arr:
    	    A[i]+=1
    	
    	for i in range(n):
    	    
    	    if A[i]>1:
    	        b.append(i)
    	
    	if len(b) != 0:
    	    return b
    	else:
    	    return [-1]
    	    

#{ 
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends