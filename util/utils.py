from config import OUTPUT_DELIMITER, VALID_OP, DELIMITER

def log(s):
    # print(">> {}".format(s))
    print("ERROR: {}".format(s))

def processInput(l):
    args = l.split(" ")
    op = args.pop(0)
    data = " ".join(args)

    return op, data, args

def processLine(line):
    line = line.replace("\n", "").replace(DELIMITER, OUTPUT_DELIMITER)
    return line

def getOP(l):
    # return l.split(DELIMITER)[0]
    return l.split(" ")[0]

def isValidOP(op):
    return op in VALID_OP

def isValidInputData(schemaLen, args):
    return len(args) == schemaLen

def isInt(s):
    try:
        temp = int(s)
        return True
    except ValueError:
        return False