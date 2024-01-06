import os
import time

import requests
from tqdm import tqdm

f_train = open('fashion_train.txt', "r")
f_test = open('fashion_test.txt', "r")

train_files = f_train.readlines()
test_files = f_test.readlines()

# os.mkdir('train')
# os.mkdir('test')

req_headers = {
    'Connection': 'close',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
timeout = 5
for video_url in tqdm(train_files):
    file_name = video_url[:-1].split("/")[-1]
    out_file = f"train/{file_name}"
    if os.path.exists(out_file):
        continue
    try:
        r = requests.get(
            video_url[:-1], 
            headers=req_headers,
            timeout=timeout
        )
    except Exception as e:
        print(e)
        continue
    with open(out_file, 'wb') as f:
        f.write(r.content)
    time.sleep(1)

for video_url in tqdm(test_files):
    file_name = video_url[:-1].split("/")[-1]
    out_file = f"test/{file_name}"
    if os.path.exists(out_file):
        continue
    try:
        r = requests.get(
            video_url[:-1], 
            headers=req_headers,
            timeout=timeout
        )
    except Exception as e:
        print(e)
        continue
    with open(out_file, 'wb') as f:
        f.write(r.content)
