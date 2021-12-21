import requests
TOTAL_PAGES = 241

for i in range(0, TOTAL_PAGES):
    print(str(i).zfill(len(str(TOTAL_PAGES))))

    #requesting page...
    response = requests.get("https://resources.pearsonactivelearn.com/r00/r0062/r006201/r00620161/current/OPS/images/577991-" + str(i).zfill(3) + ".jpg", stream=True)

    if not response.ok:
        #failed
        print(response)
        
    if response.ok:
        #success, download the image
        with open("577991-" + str(i).zfill(len(str(TOTAL_PAGES))) + ".jpg", 'wb') as handle:
            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)
