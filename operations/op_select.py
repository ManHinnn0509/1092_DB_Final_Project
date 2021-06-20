from util.file_utils import isEmptyFile
from util.utils import log, processLine
from config import DB_FILE_NAME, DELIMITER
from schema import KEY_INDEX_DICT

SHOW_KEYWORD = "SHOW"

# Format examples:
# SELECT 企管一甲 SHOW 開課班級 課程名稱 選課代號
# SELECT * SHOW 開課班級 課程名稱 選課代號

def select(l):
    if (isEmptyFile(DB_FILE_NAME)):
        log("Database is empty!")
        return
    
    if (SHOW_KEYWORD not in l):
        __simpleSelect(l)
    else:
        __showSelect(l)

def __simpleSelect(l):
    l = l.split(" ")

    key = l[-1]
    if (key == "*"):
        key = ""

    with open(DB_FILE_NAME, "r", encoding="utf-8") as f:
        next(f)
        for line in f:
            if (line == "\n"):
                continue
            if (line.startswith(key)):
                line = processLine(line)
                print(f"\t{line}")

def __showSelect(l):
    l = l.split(" " + SHOW_KEYWORD + " ")

    key = l[0].split(" ")[-1]
    # print(key)
    if (key == "*"):
        key = ""

    show = l[-1].split(" ")
    # print(show)

    indexList = []
    for s in show:
        if (s == ""):
            continue
        i = __getIndex(s)
        if (i == -1):
            log("Invalid header detected!")
            return
        indexList.append(i)
    
    with open(DB_FILE_NAME, "r", encoding="utf-8") as f:
        next(f)
        for line in f:
            if (line == "\n"):
                continue
            if (line.startswith(key)):
                line = __formatLine(line, indexList)
                print(f"\t{line}")

def __formatLine(line, indexList):
    line = processLine(line)
    line = line.split(" ")

    l = ""
    for i in indexList:
        l += line[i] + " "
    return l

def __getIndex(key):
    return KEY_INDEX_DICT.get(key, -1)