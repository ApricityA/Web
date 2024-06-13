from utils.utils import *

def getDir_top20():
    dirDataList = typeList('directors')
    dirDataObj = {}
    for dir in dirDataList:
        if dir not in dirDataObj:
            dirDataObj[dir] = 1
        else:
            dirDataObj[dir] += 1
    dirData = sorted(dirDataObj.items(), key=lambda x: x[1], reverse=True)[:20]
    dirRow = []
    dirColumns = []
    for i in dirData:
        dirRow.append(i[0])
        dirColumns.append(i[1])
    return dirRow, dirColumns

def getActor_top20():
    actorDataList = typeList('casts')
    actorDataObj = {}
    for actor in actorDataList:
        if actor not in actorDataObj:
            actorDataObj[actor] = 1
        else:
            actorDataObj[actor] += 1
    actorData = sorted(actorDataObj.items(), key=lambda x: x[1], reverse=True)[:20]
    actorRow = []
    actorColumns = []
    for i in actorData:
        actorRow.append(i[0])
        actorColumns.append(i[1])
    print(actorData, actorRow, actorColumns)
    return actorRow, actorColumns
