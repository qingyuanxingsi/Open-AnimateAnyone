import csv
import os

dataset_folder = 'datasets/UBC_dataset'
splits = ['train','test']

for split in splits:
    csv_path = os.path.join(dataset_folder, f'{split}_info.csv')
    split_folder = os.path.join(dataset_folder, split)
    with open(csv_path, 'w', newline='') as csvfile:
        fieldnames = ['folder_id', 'folder_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i, folder in enumerate(os.listdir(split_folder)):
            folder_path = os.path.join(split_folder, folder)
            writer.writerow({'folder_id': i + 1, 'folder_name': folder.split(".")[0]})
