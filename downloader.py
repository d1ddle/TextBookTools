import requests

# EDIT THESE BEFORE RUNNING TO CHANGE THE BOOK DOWNLOAD
TOTAL_PAGES = 241
URL_PREFIX = "https://resources.pearsonactivelearn.com/r00/r0062/r006201/r00620161/current/OPS/images/577991-"
URL_SUFFIX = ".jpg"


# DONT TOUCH PAST HERE UNLESS YOU KNOW WHAT YOUR DOING
print("\nTrying for book starting at URL: " + URL_PREFIX + str(1).zfill(3) + URL_SUFFIX + "\n")

for i in range(0, TOTAL_PAGES):
    print(str(i).zfill(len(str(TOTAL_PAGES))))

    #requesting page...
    response = requests.get(URL_PREFIX + str(i).zfill(3) + URL_SUFFIX, stream=True)

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
