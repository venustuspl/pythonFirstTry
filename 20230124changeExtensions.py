import glob, os
from datetime import datetime
path = os.path.abspath(os.getcwd())
os.path.abspath(path)
now = datetime.now().strftime("%Y%b%d")

for file in glob.glob("*.xml"):
    os.rename(file, file + "Q" + now)
    print(file)
