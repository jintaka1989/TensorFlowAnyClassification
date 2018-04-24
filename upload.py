import os
import sys

argvs = sys.argv

os.system('git add .')
if len(argvs) < 2:
    commit_message = "push using upload.py"
else:
    commit_message = str(argvs[1])

os.system('git commit -m ' + '"' + commit_message + '"')
os.system('git push')
