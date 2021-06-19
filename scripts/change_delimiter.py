dirName = "scripts"
dataTemplateName = "data_template.txt"

p = "./{}/{}".format(dirName, dataTemplateName)

f = open(p, "r", encoding="utf-8")
content = f.read()
f.close()

DELIMITER_FROM = ","
DELIMITER_TO = ","

content = content.replace(DELIMITER_FROM, DELIMITER_TO)

outputFileName = "data.txt"
outputPath = "./{}/{}".format(dirName, outputFileName)

f = open(outputPath, "w+", encoding="utf-8")
f.write(content)
f.close()

print("--- End of Program ---")