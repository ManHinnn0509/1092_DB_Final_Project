def readFirstLine(p):
    l = None
    with open(p, encoding="utf-8") as f:
        l = f.readline()
    return l

"""
# This shouldn't be used because of the limitation
def readFileToList(p, utf8 = True):
    encoding = "utf-8" if (utf8) else "ascii"

    f = open(p, "r", encoding=encoding)
    content = f.read()
    f.close()

    l = content.split("\n")
    return l
"""