
# TikTok-ify

Convert two videos into a dopamine-overloaded TikTok!



# Usage
1. Run `python main.py`
2. Fill in the arguements (or press 'enter' to use the defualt config)
3. Wait for the program to finish.

# Installation
1. Using git
```
git clone https://ctih1/TikTokify
cd TikTokify
pip install -r requirements.txt
cd src
python main.py
```

# File structure
```
/input location
    /background
        1.mp4
    /foreground
        1.mp4
```

# Arguements
- Input location \
    A folder where two sub-folders exist:

- Output location: \
    A folder where the .mp4 file will be saved.

- File name: \
    The file name. (name.mp4 and name both work)

- FPS: \
    The framerate of the final video

- Threads: \
    How many threads ffmpeg will use.