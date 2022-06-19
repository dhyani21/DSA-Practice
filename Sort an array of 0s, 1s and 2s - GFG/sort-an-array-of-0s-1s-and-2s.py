#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        c = arr.count(0)
        c1 = arr.count(1)
        c2 = arr.count(2)
        #for i in range(n):
        #   if arr[i] == 0:
         #       c += 1
          #  if arr[i] == 1:
           #     c1 += 1
            #if arr[i] == 2:
             #   c2 += 1
        arr[0:c] = [0] * c
        arr[c:c + c1] = [1] * c1
        arr[c+c1: c+c1+c2] = [2] * c2
        return arr
        


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends