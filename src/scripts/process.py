from moviepy.video.fx.crop import crop
from moviepy.editor import VideoFileClip
from . import tools
from moviepy.video.fx.resize import resize
from moviepy.editor import VideoFileClip, concatenate_videoclips

last_height: int or float = 0

def _crop(_clip_: VideoFileClip, full_resolution: list, bottom_clip: bool) -> VideoFileClip:
    print("TT:fy - Resizing")
    x: int = full_resolution[0]
    y: int = full_resolution[1]
    
    _clip_ = _clip_[0]
    
    (width, height) = _clip_.size
    if bottom_clip:
        crop_height = width * 5/6
    else:
        crop_height = width * 5/4
        
    y1,y2 = (height - crop_height)//2, (height + crop_height)//2
    x1,x2 = 0, width
    
    new_clip = crop(
        _clip_,
        x1=x1,
        x2=x2,
        y1=y1,
        y2=y2,
    )
    
    new_clip.size = [x,new_clip.size[1]]
    
    print("TT:fy - Done resizing")
    return new_clip

def _resize(clip: VideoFileClip, bottom_clip:bool, resolution:list) -> VideoFileClip:
    global last_height
    if not bottom_clip:
        clip = resize(
            clip, 
            newsize=[
                resolution[0], 
                ((resolution[0]) / 15) * 16
            ]
        )
        last_height = ((resolution[0]) / 15) * 16
    else:
        clip = resize(
            clip,
            newsize=[
                resolution[0],
                ((resolution[0] / 45 )) * 32
            ]
        )
    return clip

def repeat_back(clip: VideoFileClip, target_len: int) -> VideoFileClip:
    if clip.duration >= target_len:
        return clip
    clips: list = []
    target: int = int(target_len) // int(clip.duration)
    total_lenght: int = 0
    
    for i in range(target):
        clips.append(clip)
            
    clip = concatenate_videoclips(clips)
    return clip