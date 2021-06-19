from util.utils import isValidInputData, processInput, log

from config import DB_FILE_NAME

def insert(SCHEMA_LEN, l):
    op, data, args = processInput(l)

    if not (isValidInputData(SCHEMA_LEN, args)):
        log("Invalid input data!")
        return
    
    if (__isDupelicated(data)):
        log("Duplicated data detected!")
        return
    
    r = __addRow(data)
    if (r):
        print("Added data [{}] into database".format(data))

def __isDupelicated(data):
    with open(DB_FILE_NAME, "r", encoding="utf-8") as f:
        for line in f:
            if (line == "\n"):
                continue
            
            line = line.replace("\n", "")
            if (line == data):
                return True
    
    return False

def __addRow(data):
    try:
        f = open(DB_FILE_NAME, "a", encoding="utf-8")
        f.write(str(data) + "\n")
        f.close()

        return True
    except:
        return False