
from scripts.generate_script import generate_script
from scripts.generate_voice import generate_voice
from scripts.generate_visuals import get_videos
from scripts.generate_viral_subtitles import generate_viral_srt
from scripts.render_video import render
import uuid, os

def generate_batch(total):
    os.makedirs("output", exist_ok=True)
    os.makedirs("temp", exist_ok=True)

    for i in range(total):
        text = generate_script()
        voice = generate_voice(text)

        srt_text = generate_viral_srt(text, 30)
        srt_path = f"temp/{uuid.uuid4()}.srt"
        with open(srt_path, "w", encoding="utf-8") as f:
            f.write(srt_text)

        videos = get_videos(6)
        output = f"output/short_{uuid.uuid4()}.mp4"

        render(
            video_files=videos,
            voice_path=voice,
            music_path="assets/music/ambient.mp3",
            srt_path=srt_path,
            output_path=output
        )

        print(f"Vídeo {i+1}/{total} criado")
      
