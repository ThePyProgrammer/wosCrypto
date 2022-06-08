def extendedEuclidean(a, b):
    if a < b: b, a = a, b
    lst = []
    while b:
        lst.append([a, a//b, b, a%b])
        