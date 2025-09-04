def fibonacci(n):
    a = 1
    b = 1
    
    series = []
    if n < 2:
        series.append(a)
        return series
    elif n == 2:
        series.append(a)
        series.append(b)
        return series
    
    series.append(a)
    series.append(b)
    for i in range(2, n):
        series.append(series[i-1] + series[i-2])
    
    return series

print(fibonacci(10))