import os
import shutil
import argparse

def split_files_into_folders(root_folder):
    print(f"Sorting files in {root_folder}.")

    # Creating path for each subfolder
    music_folder = os.path.join(root_folder, "music")
    documents_folder = os.path.join(root_folder, "documents")
    videos_folder = os.path.join(root_folder, "videos")
    pictures_folder = os.path.join(root_folder, "pictures")
    others_folder = os.path.join(root_folder, "others")

    # Creating the subfolders if they don't exist
    os.makedirs(music_folder, exist_ok=True)
    os.makedirs(documents_folder, exist_ok=True)
    os.makedirs(videos_folder, exist_ok=True)
    os.makedirs(pictures_folder, exist_ok=True)
    os.makedirs(others_folder, exist_ok=True)

    # List all the files in the root folder
    for filename in os.listdir(root_folder):
        file_path = os.path.join(root_folder, filename)
        if os.path.isfile(file_path):
            _, file_extension = os.path.splitext(file_path)

            # Move the file to the appropriate subfolder
            if file_extension in [".mp3", ".flac", ".aac", ".wav",".asd",".m4a"]:
                destination_folder = music_folder
            elif file_extension in [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",".txt"]:                
                destination_folder = documents_folder
            elif file_extension in [".mp4", ".mkv", ".avi",".wmv"]:
                destination_folder = videos_folder
            elif file_extension in [".jpg", ".jpeg", ".png", ".gif",".bmp"]:
                destination_folder = pictures_folder
            else:
                destination_folder = others_folder
            
            # Checking if file already exists in destination
            if os.path.exists(os.path.join(destination_folder,filename)):
                choice = input(f"{destination_folder} already exists, do you want to overwrite the file? (y/n)")
                if choice.lower() == 'y':
                    shutil.copy2(file_path, destination_folder)
                    os.remove(file_path)
                    print(f"Overwritten {filename} to {destination_folder}")
                else:
                    print("file was not copied")
            else:
                shutil.move(file_path, destination_folder)
                print(f"Moved {filename} to {destination_folder}")

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description='Split files into subfolders')
        parser.add_argument('path', type=str, nargs='?', help='Path to the folder')
        args = parser.parse_args()
    except Exception as e:
        print(f"error while getting arguments: {e}")

    try:
        path = args.path
        if args.path is None:
            choice = input(f"No directory provided, do you want to use the present working directory {os.getcwd()}? (y/n) ")
            if choice.lower() != 'y':
                print("Exiting...")
                exit()
            path = os.getcwd()
        elif not os.path.exists(path):
            choice = input(f"The directory {path} does not exist, do you want to use the present working directory {os.getcwd()} instead? (y/n) ")
            if choice.lower() != 'y':
                print("Exiting...")
                exit()
            path = os.getcwd()
    except Exception as e:
        print(f"error while validating arguments: {e}")

    try:
        split_files_into_folders(path)
    except Exception as e:
        print(f"error while moving files: {e}")
