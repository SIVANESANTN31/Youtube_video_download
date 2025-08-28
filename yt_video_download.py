

import os
import yt_dlp

VIDEO_URL = "https://youtu.be/NW6Dgax2d6I?si=wMMchQXnLRHBrfHv"
OUTPUT_DIR = "yt_video_downloads"

def download_video_with_audio(url, outdir):
    """Download YouTube video with audio merged into single MP4"""
    ydl_opts = {
        'format': 'bestvideo+bestaudio',        # pick best video + audio
        'merge_output_format': 'mp4',           # merge into mp4
        'outtmpl': f'{outdir}/%(title)s.%(ext)s',
    }

    os.makedirs(outdir, exist_ok=True)

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

print("⬇️ Downloading video with audio (merged MP4)...")
download_video_with_audio(VIDEO_URL, OUTPUT_DIR)
print("✅ Done! Single MP4 saved in", OUTPUT_DIR)
