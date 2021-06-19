from config import VALID_OP, DELIMITER

def log(s):
    # print(">> {}".format(s))
    print("ERROR: {}".format(s))

def processInput(l):
    args = l.split(" ")
    op = args.pop(0)
    data = " ".join(args)

    return op, data, args

def getOP(l):
    return l.split(DELIMITER)[0]

def isValidOP(op):
    return op in VALID_OP

def isValidInputData(SCHEMA_LEN, args):
    return len(args) == SCHEMA_LEN