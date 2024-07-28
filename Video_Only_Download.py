import yt_dlp
import os
import time

def download_video(url, output_path):
    ydl_opts = {
        'outtmpl': output_path,  # Output path with filename template
        'format': 'bestvideo+bestaudio/best',  # Select the best quality for video and audio
        'merge_output_format': 'mp4',  # Ensure the final output is in mp4 format
        'postprocessors': [{  # Ensure that only the final combined file is kept
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'cleanup': True  # Remove intermediate files (default behavior)
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except Exception as e:
            print(f"Failed to download {url}: {e}")

def download_from_file(file_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    with open(file_path, 'r') as file:
        urls = file.readlines()
    
    for i, url in enumerate(urls):
        url = url.strip()
        if url:
            timestamp = int(time.time())
            filename = f"video_{timestamp}_{i}.%(ext)s"
            output_path = os.path.join(output_folder, filename)
            print(f"Downloading {url} to {output_path}")
            download_video(url, output_path)

if __name__ == "__main__":
    links_file = 'extract_links.txt'
    output_folder = 'hello'
    download_from_file(links_file, output_folder)

