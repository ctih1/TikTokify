import os
from scripts import files, render, process, position
import json

save_location: str = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "input","config","config.json"))

modified: bool = False
print("Welcome to Tiktokify - Fair Videos made Easy")
print("Press 'enter' to use the default setting.")

settings: dict = {}

resolution: list = [720,1280]

with open(save_location,"r") as f:
    try:
        settings = json.load(f)
        settings["load_from_json"] = True
    except json.JSONDecodeError:
        settings = {}
        

print(settings)    
if settings.get("input_loc",None) == None:
    _input_ = input("Input location: ").strip()
    if _input_ != "":
        settings["input_loc"] = _input_
        modified=True
        
if settings.get("output_loc",None) == None:
    _input_ = input("Output location: ").strip()
    if _input_ != "":
        settings["output_loc"] = _input_
        modified=True
        
if settings.get("output_file",None) == None:
    _input_ = input("File name: ").strip()
    if _input_ != "":
        if not _input_.endswith(".mp4"):
            _input_ = _input_ + ".mp4"
        settings["output_file"] = _input_
        modified=True
if settings.get("fps",None) == None:
    _input_ = input("FPS: ").strip()
    if _input_ != "":
        settings["fps"] = _input_
        modified=True
if settings.get("threads",None) == None:
    _input_ = input("Threads: ").strip()
    if _input_ != "":
        settings["threads"] = _input_ 
        modified=True
        
if modified:
    _input_ = input("Save settings?\ntrue/false: ")
    if _input_.lower() == "true":
        with open(save_location,"w") as f:
            json.dump(settings,f,indent=2)

top_clip_duration: int or float = files.get_files(settings.get("input_loc",os.path.abspath(os.path.join(os.path.dirname( __file__ ), "..", "input"))))[1][0].duration
  
render.render(
    position.position(
        upper=process._resize(
            clip=process._crop(
                files.get_files(settings.get("input_loc",os.path.abspath(os.path.join(os.path.dirname( __file__ ), "..", "input"))))[1],
                resolution,
                bottom_clip=False
            ),
            resolution=resolution,
            bottom_clip=False
        ),
        bottom=process.repeat_back(
            clip=process._resize(
                clip=process._crop(
                        files.get_files(settings.get("input_loc",os.path.abspath(os.path.join(os.path.dirname( __file__ ), "..", "input"))))[0],
                        resolution,
                        bottom_clip=True
                    ),
                bottom_clip=True,
                resolution=resolution
            ),
            target_len=top_clip_duration
        ),
        resolution=resolution
    ),
    settings.get("output_loc",os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "output"))),
    settings.get("output_file","result.mp4"),
    fps=int(settings.get("fps",30)),
    threads=int(settings.get("threads",2))
)
