def generate_viral_srt(text, duration):
    words = text.split()
    srt = ""
    index = 1
    time_per_word = duration / max(len(words), 1)
    current_time = 0

    for word in words:
        start = current_time
        end = current_time + time_per_word

        srt += f"{index}\n"
        srt += f"00:00:{start:05.2f} --> 00:00:{end:05.2f}\n"
        srt += f"{word.upper()}\n\n"

        current_time = end
        index += 1

    return srt
  
