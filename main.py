import os

from util.utils import log, getOP
from config import DB_FILE_NAME, DELIMITER

from operations import *

"""
    Header:
        開課班級 課程名稱 選課代號 學分數 必選修 開課單位 開課人數 已收授人數 授課教師
"""

def main():
    while (True):
        l = input(">> ")
        if (l == ""):
            continue

        op = getOP(l).upper()
        if (op == "EXIT"):
            break
        elif (op == "EXPORT"):
            export(l)
        elif (op == "INSERT"):
            insert(l)
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