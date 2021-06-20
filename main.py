from operations.op_delete import delete
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
"""

SCHEMA_LEN = 9

def main():
    while (True):
        l = input()
        if (l == ""):
            continue

        op = getOP(l).upper()
        if (op == "EXIT"):
            break
        elif (op == "EXPORT"):
            export(l)
        elif (op == "INSERT"):
            insert(SCHEMA_LEN, l)
        elif (op == "SELECT"):
            select(l)
        elif (op == "DELETE"):
            delete(l)
        else:
            log("[{}] is an invalid OP!".format(op))

if (__name__ == "__main__"):
    os.system("cls")

    # Fixed schema... = =
    # SCHEMA_LEN = len(readFirstLine(DB_FILE_NAME).split(DELIMITER))

    main()