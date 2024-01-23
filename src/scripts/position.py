from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip
from . import tools


def position(bottom: VideoFileClip, upper: VideoFileClip, resolution: list) -> VideoFileClip:
    """_summary_

    Args:
        bottom (VideoFileClip): The lower clip. (5/4)
        upper (VideoFileClip): The upper clp (3/4)
        resolution (list): Resolution [width, height]
    Returns:
        VideoFileClip: combined video.
    """
    combined_clip: VideoFileClip or CompositeVideoClip

    
    upper = upper.set_position(("center","top"))
    bottom = bottom.set_position(("center",upper.h))
    bottom = bottom.set_duration(upper.duration)
    
    combined_clip = CompositeVideoClip(clips=[bottom, upper], size=resolution)
    return combined_clip