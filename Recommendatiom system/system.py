def coff(k):
    return (round((k/ 5.0), 2))

def check(n):
    if n == 1 or n == 2:
        return n
    elif 3 <= n <= 8:
        return 3
    elif 9 <= n <= 16:
        return n // 3
    else:
        return 6

