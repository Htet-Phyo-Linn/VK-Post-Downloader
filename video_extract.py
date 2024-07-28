from header import *

def extract_video_urls(url):
    ydl_opts = {
        'noplaylist': True,  # Only extract single video URLs, not playlists
    }

    video_urls = []

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        entries = info_dict.get('entries', [info_dict])

        for entry in entries:
            video_url = entry['webpage_url']
            video_urls.append(video_url)
            print(f"Extracted URL: {video_url} \n")

    return video_urls

