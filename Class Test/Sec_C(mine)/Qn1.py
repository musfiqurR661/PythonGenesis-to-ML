myDict = {
    'Mus': 78,
    'Fiq': 87,
    'tas': 40,
    'nom': 30,
    'ovi': 20
}


def func(myDict):
    list = []
    for a in myDict:
        if myDict[a] > 60:
            list.append(a)
    return list.reverse()


az = func(myDict)
print(az)
