def dynamicArray(n, queries):
    seqList = [[] for i in range(n)]
    lastAnswer = 0
    rtn = []

    for query in queries:
        if query[0] == 1:
            seqList[(query[1] ^ lastAnswer) % n].append(query[2])
        else:
            lastAnswer = seqList[(query[1] ^ lastAnswer) % n][query[2] % len(seqList[(query[1] ^lastAnswer) % n])]
            rtn.append(lastAnswer)
            
    return rtn


if __name__ == '__main__':
    print([[1]*2])
