# Wipe file content

import os

p = "./lab/TextFile.txt"
open(p, "w+", encoding="utf-8").close()

b = (os.stat(p).st_size == 0)
print(b)