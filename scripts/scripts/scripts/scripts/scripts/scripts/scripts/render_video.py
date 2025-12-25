from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, CompositeAudioClip, TextClip, CompositeVideoClip
import os

def render(video_files, voice_path, music_path, srt_path, output_path):
    clips = []

    for v in video_files:
        clip = VideoFileClip(v).subclip(0, 5).resize((1080, 1920))
        clips.append(clip)

    video = concatenate_videoclips(clips, method="compose")

    voice = AudioFileClip(voice_path)
    music = AudioFileClip(music_path).volumex(0.2)

    audio = CompositeAudioClip([music, voice])
    video = video.set_audio(audio)

    final = video.set_duration(voice.duration)

    final.write_videofile(
        output_path,
        fps=30,
        codec="libx264",
        audio_codec="aac"
    )
  
