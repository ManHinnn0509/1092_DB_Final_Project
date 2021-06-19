import os

from util.utils import log, processInput, isValidOP, getOP
from util.file_utils import readFirstLine
from config import DB_FILE_NAME, DELIMITER

from operations.op_insert import insert
from operations.op_select import select

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

        if (op == "INSERT"):
            insert(SCHEMA_LEN, l)

if (__name__ == "__main__"):
    os.system("cls")

    # Fixed schema... = =
    # SCHEMA_LEN = len(readFirstLine(DB_FILE_NAME).split(DELIMITER))
    SCHEMA_LEN = 9

    main()