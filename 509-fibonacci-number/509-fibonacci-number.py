class Solution:
    def fib(self, n: int) -> int:
        if n==1:
            return n
        if n==0:
            return 0
        else:
            return self.fib(n-1)+self.fib(n-2)
        
        
        