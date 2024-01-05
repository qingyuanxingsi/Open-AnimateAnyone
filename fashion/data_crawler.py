import requests
import os
from tqdm import tqdm
import time

f_train = open('fashion_train.txt', "r")
f_test = open('fashion_test.txt', "r")

train_files = f_train.readlines()
test_files = f_test.readlines()

# os.mkdir('train')
# os.mkdir('test')

for video_url in tqdm(train_files):
    r = requests.get(video_url[:-1], headers={'Connection': 'close'})
    file_name = video_url[:-1].split("/")[-1]
    out_file = f"train/{file_name}"
    if os.path.exists(out_file):
        continue
    with open(out_file,'wb') as f:
        f.write(r.content)
    time.sleep(1)

for video_url in tqdm(test_files):
    r = requests.get(video_url[:-1], headers={'Connection': 'close'})
    file_name = video_url[:-1].split("/")[-1]
    out_file = f"test/{file_name}"
    if os.path.exists(out_file):
        continue
    with open(out_file,'wb') as f:
        f.write(r.content)
