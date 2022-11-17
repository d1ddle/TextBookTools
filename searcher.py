import requests, os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko)',
    'From': 'js9553938@gmail.com'  # This is another valid field
}

SEARCH_ROOT = "https://assets-runtime-production-oxed-oup.avallain.net/ebooks/d214cd0758181013c16ab8b1/images/page-"
SEARCH_SUFFIX = ".jpg"
SEARCH_TERM = "00000000000000000000000000000000"

print(int(SEARCH_TERM+1))
