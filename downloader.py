import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko)',
    'From': 'js9553938@gmail.com'  # This is another valid field
}

# EDIT THESE BEFORE RUNNING TO CHANGE THE BOOK DOWNLOAD
TOTAL_PAGES = 241
URL_PREFIX_VIVA = "https://resources.pearsonactivelearn.com/r00/r0062/r006201/r00620161/current/OPS/images/577991-"
URL_PREFIX_CHEM = "https://assets-runtime-production-oxed-oup.avallain.net/ebooks/32901d8ab3919c171453f0bd/images/"
URL_PREFIX = URL_PREFIX_CHEM
URL_SUFFIX = ".jpg"


# DONT TOUCH PAST HERE UNLESS YOU KNOW WHAT YOUR DOING
print("\nTrying for book starting at URL: " + URL_PREFIX + str(1).zfill(3) + URL_SUFFIX + "\n")

for i in range(0, TOTAL_PAGES):
    print(str(i).zfill(len(str(TOTAL_PAGES))))

    #requesting page...
    response = requests.get(URL_PREFIX + str(i).zfill(3) + URL_SUFFIX, stream=True, headers=headers)

    if not response.ok:
        #failed
        print(response)
        
    if response.ok:
        #success, download the image
        with open(URL_PREFIX.split("/")[-1] + str(i).zfill(len(str(TOTAL_PAGES))) + URL_SUFFIX, 'wb') as handle:
            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)
