# Print Current Directory

import os
#print(os.getcwd())
path = os.walk(os.getcwd())
for i, j , k in path:
    print("dir path\n", i)
    print("fol\n", j)
    print("file\n", k)