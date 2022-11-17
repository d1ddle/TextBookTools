import os, time
from fpdf import FPDF
imagelist = []
FOLDER_NAME = "ENGLLANG-REVISE-EDEXCELGCSE(9-1)"
PDF_NAME = "ENGLLANG-REVISE-EDEXCELGCSE(9-1).pdf"
FILENAME_PREFIX = "EdexEngLangRG-"
PLACE_HOLD_NO = 2
IMG_WIDTH = 210
IMG_HEIGHT = 265
TOTAL_IMAGES = 293

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

PLACE_HOLD_NO += 1
FAILS = 0

for i in range(1, TOTAL_IMAGES):
    if FAILS >= 3:
        break
    new_find = str(find(FILENAME_PREFIX + str(i).zfill(PLACE_HOLD_NO) + ".jpg", "./" + FOLDER_NAME))
    print("\rFOUND " + new_find, end="")
    if new_find != "None":
        imagelist.append(new_find)
        FAILS = 0
    else:
        FAILS += 1

pdf = FPDF('P', 'mm', (IMG_WIDTH, IMG_HEIGHT))
# imagelist is the list with all image filenames
i = 1
for image in imagelist:
    pdf.add_page()
    pdf.image(image,0,0,IMG_WIDTH,IMG_HEIGHT,type='JPG')
    
pdf.output("./" + PDF_NAME, "F")
print("COMPLETED MAKING PDF! YAY")
input("Press Any Key to Continue")
time.sleep(15)
