# Using tabulation

def fib(n: int) -> int:
        fibonaccis = [0, 1]
        if n < 2: return fibonaccis[n]
        
        for i in range(n):
            if len(fibonaccis) > n:
                return fibonaccis[n]
            fibonaccis.append(fibonaccis[i] + fibonaccis[i+1])
    
print(fib(3))