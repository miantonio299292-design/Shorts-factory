import random
import glob

def get_videos(qty=6):
    videos = glob.glob("assets/videos/*.mp4")
    return random.sample(videos, min(qty, len(videos)))
  
