def minimal(v1, v2, v3, v4):
    min = 0
    if v1 < v2:
        min = v1
    if v2 < v3:
        min = v2
    elif v3 < v4:
        min = v3
    elif v4 < v3:
        min = v4
    print("min value is: ", min)
    
minimal(4, 1, 2, 3)
    