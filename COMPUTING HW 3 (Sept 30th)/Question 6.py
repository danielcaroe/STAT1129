def power(num):
    n = 1;
    while n in range(num):
        if int(n) < int(num):
            print(n, n**n)
        else:
            print('greater than', num)
        n = n + 1
        
power(8)