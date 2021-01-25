# Place this script in the folder that
# contains the files you want to remove spaces from

import os

if __name__ == "__main__":
    for filename in os.listdir("."):
        os.rename(filename, filename.replace(" ", ""))
