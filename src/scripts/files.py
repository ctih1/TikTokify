import os
from moviepy.editor import VideoFileClip

def get_files(video_location: str) -> list:
    print("TT:fy - Loading file...")
    foreground_clips: list = []
    background_clips: list = []
    for video in os.listdir(fr"{video_location}\background"):
        if video.endswith(".mp4"):
            background_clips.append(VideoFileClip(fr"{video_location}\background\{video}"))

    for video in os.listdir(fr"{video_location}\foreground"):
        if video.endswith(".mp4"):
            foreground_clips.append(VideoFileClip(fr"{video_location}\foreground\{video}"))
    print("TT:fy - Loaded file.")
    return [foreground_clips, background_clips]