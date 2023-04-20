import os
import requests

sound_urls = ["https://github.com/TheBigCarrot/PyTrolls/raw/main/knock1.wav", "https://github.com/TheBigCarrot/PyTrolls/raw/main/knock2.wav"]

parent_directory = r"C:\Users\Public\Documents"
mp3_dir = "mp3s"

mp3_dir = os.path.join(parent_directory, mp3_dir)

#Make the directory if it doesnt exist
if not os.path.exists(mp3_dir):
    os.makedirs(mp3_dir)
else:
    print("Directory already exists!")

#Download all sounds
for url in sound_urls:
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(mp3_dir, os.path.basename(url)), "wb") as f:
            f.write(response.content)
        print(f"File saved!")
    else:
        print("Error downloading file")


#Create python script
dir_path = r'C:\Users\Public\Documents'
file_path = os.path.join(dir_path, "logger.py")

file_contents = ''