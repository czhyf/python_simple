import os
from PIL import Image
downd="/Users/a/Desktop/img/"
if __name__ == '__main__':
    for filenumber in os.listdir(downd):
            try:
                singleimg = Image.open(str(downd + filenumber))
                singleimg.close()
                if singleimg.size >= (512, 512):
                    print("满足")
                else:
                    os.remove(downd + filenumber)
            except:
                continue