import csv

from util.file_utils import readFirstLine, readSecondLine
from util.utils import isInt, log
from config import DB_FILE_NAME, DELIMITER

validFormat = ["CSV", "SQL"]
outputCSV_FileName = "db.csv"
outputSQL_FileName = "db.sql"

def export(l):

    # Should I make some changes in main.py so that I don't have to split it again here?
    outputFormat = l.split(" ")[-1]

    r = False
    outputName = ""

    if (outputFormat == "CSV"):
        outputName = outputCSV_FileName
        r = __outputCSV(outputName)
    elif (outputFormat == "SQL"):
        outputName = outputSQL_FileName
        r = __outputSQL(outputName)
    else:
        log("Invalid output format!")
        return
    
    if (r):
        print("Database exported. Output file name: {}".format(outputName))
    else:
        log("Unable to export [{}]".format(outputName))

def __outputCSV(outputFileName):
    # I think I'm gonna go with this way... 
    # Since I'm not sure the shorter verions will violate the limitation or not

    try:
        # utf-8-sig??? See: https://www.796t.com/article.php?id=14537
        f = open(outputFileName, "w", newline="", encoding="utf-8-sig")
        writer = csv.writer(f, delimiter = ",")

        with open(DB_FILE_NAME, "r", encoding="utf-8") as db:
            for l in db:
                if (l == "\n"):
                    continue
                l = l.replace("\n", "")
                l = l.split(DELIMITER)
                # print(l)

                writer.writerow(l)
        
        f.close()
        return True
    except Exception as e:
        print(e)
        return False

def __outputSQL(outputName):
    OUTPUT_DB_NAME = "courses_data"
    OUTPUT_TABLE_NAME = "courses"

    try:
        s = "-- Reference: A .sql file template generated by HeidiSQL" + "\n\n"

        # DB struct
        s += f"CREATE DATABASE IF NOT EXISTS `{OUTPUT_DB_NAME}`;" + "\n"
        # s += f"CREATE DATABASE `{OUTPUT_DB_NAME}`;" + "\n"
        s += f"USE `{OUTPUT_DB_NAME}`;" + "\n"
        s += "\n"

        # Table struct
        header = readFirstLine(DB_FILE_NAME, True)
        templateData = readSecondLine(DB_FILE_NAME, True)
        s += __buildTableStruct(OUTPUT_TABLE_NAME, header, templateData, DELIMITER) + "\n"
        s += "\n"

        with open(DB_FILE_NAME, "r", encoding="utf-8") as f:
            for l in f:
                if (l == "\n"):
                    continue
                l = l.replace("\n", "")
                l = l.split(DELIMITER)

                # Not sure if INSERT 1 by 1 is a good idea or not
                temp = "INSERT INTO {} VALUES {};".format(OUTPUT_TABLE_NAME, str(tuple(l))) + "\n"
                s += temp
        
        f = open(outputName, "w+", encoding="utf-8")
        f.write(s)
        f.close()

        return True
    except Exception as e:
        print(e)
        return False

def __buildTableStruct(tableName, header, templateData, delimiter):
    header = header.split(delimiter)
    templateData = templateData.split(delimiter)
    # print(header)

    l = len(header)

    s = f"CREATE TABLE IF NOT EXISTS `{tableName}` ("

    for x in range (0, l):
        h = header[x]
        dataType = "int" if (isInt(templateData[x])) else "varchar(32)"
        ending = "" if (x == l - 1) else ","

        temp = f"`{h}` {dataType}" + ending
        s += temp
    
    s += ") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"

    return s