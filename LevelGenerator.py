import random

simpleLevel = {"size": {"x": 30, "y": 30},
                "platforms": [{"type": "#", "count": 20},
                              {"type": "-", "count": 10}],

               }

def genBlank(x, y):
    level = []
    s = ["#"] * x
    level.append(s)
    i = 0

    while (i < y-2):
        st = [" "]*x
        st[0] = "#"
        st[x-1] = "#"
        level.append(st)
        i += 1
    level.append(s)
    # printLevel(level)
    return level

def genSimple():
    level = {}
    level.update({"level": genBlank(simpleLevel["size"]["x"], simpleLevel["size"]["x"])})
    level.update({"size": {"x": simpleLevel["size"]["x"],
                           "y": simpleLevel["size"]["y"]}
                  })

    for platform in simpleLevel["platforms"]:
        i = 0
        while (i <= platform["count"]):
            rndX = random.randint(2, simpleLevel["size"]["x"]-2)
            rndY = random.randint(2, simpleLevel["size"]["y"]-2)
            level["level"][rndY][rndX] = platform["type"]
            i += 1
    # printLevel(level)
    return level

def printLevel(level):
    for row in level["level"]:
        print(row)

genSimple()