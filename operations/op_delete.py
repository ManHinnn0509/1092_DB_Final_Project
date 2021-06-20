from util.file_utils import eraseFileContent
from util.utils import log
from config import DB_FILE_NAME

# Syntax:
# DELETE | CONFIRM
SYNTAX = "DELETE && CONFIRM"

def delete(l):
    if (l != SYNTAX):
        log("Invalid input!")
        return
    
    r = eraseFileContent(DB_FILE_NAME)
    if (r):
        print("All data has been removed.")
    else:
        log("Unable to erase database")