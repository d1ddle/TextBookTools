import requests, os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko)',
    'From': 'js9553938@gmail.com'  # This is another valid field
}

# EDIT THESE BEFORE RUNNING TO CHANGE THE BOOK DOWNLOAD
i = 1
FOLDER_NAME = "CHEMISTRY"
URL_PREFIX_VIVA = "https://resources.pearsonactivelearn.com/r00/r0062/r006201/r00620161/current/OPS/images/577991-"
URL_PREFIX = "https://assets-runtime-production-oxed-oup.avallain.net/ebooks/32901d8ab3919c171453f0bd/images/"
URL_SUFFIX = ".jpg"
PLACE_HOLD = False

# DONT TOUCH PAST HERE UNLESS YOU KNOW WHAT YOUR DOING
TOTAL_PAGES = 500
FAIL_COUNT = 0
print("STARTING TO DOWNLOAD BOOK. I HOPE YOU HAVE LEGAL RIGHTS TO...")

for i in range(0, TOTAL_PAGES):
    if FAIL_COUNT == 3:
        print("FAILED TO REQUEST THRICE. STOPPING")
        break

    #setting place holder values before requesting filename
    if PLACE_HOLD:
        PLACE_HOLDER = str(i).zfill(len(str(TOTAL_PAGES)))
    else:
        PLACE_HOLDER = str(i)

    #make folder to dump images
    if not os.path.isdir(FOLDER_NAME):
        os.mkdir("./" + FOLDER_NAME)
        print("CREATED FOLDER: " + FOLDER_NAME)

    #requesting page...
    print(URL_PREFIX + PLACE_HOLDER + URL_SUFFIX)
    response = requests.get(URL_PREFIX + PLACE_HOLDER + URL_SUFFIX, stream=True, headers=headers)

    if not response.ok:
        #failed
        FAIL_COUNT += 1
        print(response)
        
    if response.ok:
        FAIL_COUNT = 0
        #success, download the image
        with open(FOLDER_NAME + "/" + URL_PREFIX.split("/")[-1] + PLACE_HOLDER + URL_SUFFIX, 'wb') as handle:
            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)

