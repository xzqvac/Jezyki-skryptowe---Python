def pascal(numberOfRows):
    out = []
    p = [1]
    for x in range(numberOfRows):
        print(" ".join([str(s) for s in p]))
        out.append(p)
        p = [1] + [p[i]+p[i+1] for i in range(len(p)-1)]+[1]
    return out


out = pascal(10)
