boardd = ['tL', 'tM', 'tR',
          'mL','mM', 'mR',
          'bL', 'bM', 'bR']
someDict = {}
def valChecker(f, l):
    for x in valPos:
        if boardd[f][0] not in x:
            continue
        x.remove(boardd[f][0])
        if boardd[l][0] not in x:
            continue
        x.remove(boardd[l][0])
        if someDict[boardd[f] + boardd[l]][0] not in x:
            x.extend((boardd[f][0], boardd[l][0]))
            continue
        return True
    return False
def alter(x, y):
    try:
        someDict[boardd[x] + boardd[y]] = boardd[int(y * 2 - x)]
        if valChecker(x, y):
            return
        someDict[boardd[x] + boardd[y]] = boardd[int(x * 2 - y)]
        if valChecker(x, y):
            return
        del someDict[boardd[x] + boardd[y]]
    except IndexError:
        del someDict[boardd[x] + boardd[y]]
        return
    
for i in range(9):
    for o in range(i + 1, 9):
        valPos = [['t', 't', 't'], ['m', 'm', 'm'], ['b', 'b', 'b'], ['t', 'm', 'b']]
        a = (i + o) / 2
        if (i == 0 and o == 7) or (i == 1 and o == 3) or (i == 2 and o == 7):
            continue
        if a % 1 == 0:
            someDict.setdefault(boardd[i] + boardd[o], boardd[int((i + o) / 2)])
            if not valChecker(i, o):
                alter(i, o)
        else:
            someDict.setdefault(boardd[i] + boardd[o], boardd[(int(o * 2 - i)) % 9])
            if not valChecker(i, o):
                alter(i, o)
someDict['bMbR'] = 'bL' #cheapfix,comeback later to fix