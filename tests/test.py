def fib(n):
    if n < 1: return 0

    dp = [1, 1]
    for i in range(n - 2):
        dp += dp[-1] + dp[-2]
    return dp[-1]

def test_fib():
    assert fib(-1) == 0
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(10) == 55
