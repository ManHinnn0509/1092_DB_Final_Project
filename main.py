import os

from util.utils import log, processInput, isValidOP, getOP
from util.file_utils import readFirstLine
from config import DB_FILE_NAME, DELIMITER

from operations.op_export import export
from operations.op_insert import insert
from operations.op_select import select

"""
    Header:
        開課班級 課程名稱 選課代號 學分數 必選修 開課單位 開課人數 已收授人數 授課教師
    File db.txt, line 142:
        通識－人文(H) 音樂行旅 - 巡訪古典音樂大師 2915 2 O 通識核心課程 60 51 曾韻心
    Changed to:
        通識－人文(H) 音樂行旅 0000 巡訪古典音樂大師 2915 2 O 通識核心課程 60 51 曾韻心
    
    Since it has to have a Course ID (選課代號)
"""

SCHEMA_LEN = -1

def main():
    while (True):
        l = input()
        if (l == ""):
            continue

        op = getOP(l)
        op = op.upper()
        if (op == "EXIT"):
            break

        if not (isValidOP(op)):
            log("[{}] is an invalid OP!".format(op))
            continue
        
        if (op == "EXPORT"):
            export(l)
        if (op == "INSERT"):
            insert(SCHEMA_LEN, l)

if (__name__ == "__main__"):
    os.system("cls")

    # Fixed schema... = =
    # SCHEMA_LEN = len(readFirstLine(DB_FILE_NAME).split(DELIMITER))
    SCHEMA_LEN = 9

    main()