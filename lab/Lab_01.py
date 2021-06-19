labFolderName = "lab"
txtName = "TextFile.txt"

p = "./{}/{}".format(labFolderName, txtName)

with open(p) as f:
    for line in f:
        if (line == "\n"):
            continue
        print(line)