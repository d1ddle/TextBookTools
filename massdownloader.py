import requests, os, csv
filename = "book-list.csv"
fields = []
rows = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko)',
    'From': 'js9553938@gmail.com'  # This is another valid field
}
 
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
 
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

print("STARTING TO DOWNLOAD USING THE", filename)

for j in range(0, csvreader.line_num):
    i = 1
    FOLDER_NAME = rows[j][0]
    URL_PREFIX = rows[j][1]
    URL_SUFFIX = rows[j][2]
    PLACE_HOLD_NO = rows[j][3]
    if PLACE_HOLD_NO != "" and PLACE_HOLD_NO > "0": 
        PLACE_HOLD = True
    else:
        PLACE_HOLD = False

    if rows[j][1] == "Not easy to rip off":
        break
    elif rows[j][1] == "":
        break

    # DONT TOUCH PAST HERE UNLESS YOU KNOW WHAT YOUR DOING
    TOTAL_PAGES = 1000
    FAIL_COUNT = 0
    PLACE_HOLD_NO = (int(PLACE_HOLD_NO)) + 1
    print("\nDOWNLOADING", FOLDER_NAME, "BOOK. I HOPE YOU HAVE LEGAL RIGHTS TO!")

    for i in range(1, TOTAL_PAGES):
        if FAIL_COUNT == 3:
            print(" FAILED TO REQUEST THRICE. STOPPING")
            break

        #setting place holder values before requesting filename
        if PLACE_HOLD:
            PLACE_HOLDER = str(i).zfill(int(PLACE_HOLD_NO))
        else:
            PLACE_HOLDER = str(i)

        #make folder to dump images
        if not os.path.isdir(FOLDER_NAME):
            os.mkdir("./" + FOLDER_NAME)
            print("CREATED FOLDER: " + FOLDER_NAME)

        #requesting page...
        print('\nREQUESTING PAGE ' + URL_PREFIX + PLACE_HOLDER + URL_SUFFIX, end='')
        response = requests.get(URL_PREFIX + PLACE_HOLDER + URL_SUFFIX, stream=True, headers=headers)

        if not response.ok:
            #failed
            FAIL_COUNT += 1
            print(" OOPS!", response, end="")
            
        if response.ok:
            FAIL_COUNT = 0
            #success, download the image
            file = FOLDER_NAME + "/" + URL_PREFIX.split("/")[-1] + PLACE_HOLDER + URL_SUFFIX
            if not os.path.isfile(file):
                with open(file, 'wb') as handle:
                    for block in response.iter_content(1024):
                        if not block:
                            break
                        handle.write(block)

input("Press Enter to continue...")
