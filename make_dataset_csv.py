import os
import csv
import argparse


label_map = {"nega": 0, "posi": 1}

def create_csv_for_folder(root_dir, folder_name):
    folder_path = os.path.join(root_dir, folder_name)
    csv_file_path = os.path.join(root_dir, f"{folder_name}.csv")

    with open(csv_file_path, mode="w", newline="", encoding="utf-8") as file:
        csv_writer = csv.writer(file)
        for label in ["nega", "posi"]:
            label_path = os.path.join(folder_path, label)
            for filename in os.listdir(label_path):
                if filename.endswith(".mp4"):
                    video_path = os.path.join(label_path, filename)
                    csv_writer.writerow([video_path, label_map[label]])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root_dir", type=str, default="DA_dataset")
    args = parser.parse_args()

    root_dir = args.root_dir
    # train, val, test の各フォルダに対してCSVファイルを作成
    for folder in ["train", "val", "test"]:
        create_csv_for_folder(root_dir, folder)
