import os
from fpdf import FPDF
imagelist = []
FOLDER_NAME = "CHEMISTRY"
IMG_WIDTH = 210
IMG_HEIGHT = 265
TOTAL_IMAGES = 293

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

for i in range(1, TOTAL_IMAGES):
    new_find = str(find(str(i) + ".jpg", "./" + FOLDER_NAME))
    print("FOUND  " + new_find)
    if new_find != None:
        imagelist.append(new_find)

pdf = FPDF('P', 'mm', (IMG_WIDTH, IMG_HEIGHT))
# imagelist is the list with all image filenames
for image in imagelist:
    pdf.add_page()
    pdf.image(image,0,0,IMG_WIDTH,IMG_HEIGHT,type='JPG')
    
pdf.output("./" + FOLDER_NAME + "/ChemTriple.pdf", "F")
print("COMPLETED MAKING PDF! YAY")
