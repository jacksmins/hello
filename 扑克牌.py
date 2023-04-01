import time

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

start_time = time.time()
n = int(input("请输入一个正整数："))
print(prime_factors(n))
end_time = time.time()
print("运行时间：", end_time - start_time)
