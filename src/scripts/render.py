from moviepy.editor import VideoFileClip, concatenate_videoclips
import proglog
import os

def render(clip: VideoFileClip, path: str, filename: str, fps: int, threads:int) -> None:
    print(f"TT:fy - Rendering: {clip.size}...")
    clip.write_videofile(fr"{path}\{filename}", logger=proglog.TqdmProgressBarLogger(print_messages=False), fps=fps, threads=threads)
    print("Finished!")
    os.system(fr"start {path}\{filename}")