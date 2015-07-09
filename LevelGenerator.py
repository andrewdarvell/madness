
def genBlank(x, y):
    map = []
    s = "-" * x
    map.append(s)
    i = 0
    while (i < y-2):
        st = "-"+" " * (x-2)+"-"
        map.append(st)
        i+=1
    map.append(s)
    return map

genBlank(10, 5)
