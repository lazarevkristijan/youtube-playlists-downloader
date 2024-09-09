import yt_dlp
from concurrent.futures import ThreadPoolExecutor, as_completed

playlists = ["https://www.youtube.com/watch?v=wQruxjlJSNs&list=PLXqQwLi6dqjNgmvsZpwWmv99wYAYxiudF",
             "https://www.youtube.com/watch?v=YhkXoWvp1CU&list=PLC936F53653ECDE1C",
             "https://www.youtube.com/watch?v=LVWajJLIvnE&list=PLf8-fHlyR7DAQTYXafzlTcYYLfqXYT3iC",
             "https://www.youtube.com/watch?v=R4QGZ3L1iuI&list=PLiCkZ2lv-3aqkvdxWOBtXIjzSmCuy8cFW",
             "https://www.youtube.com/watch?v=q2fGw1zBdaM&list=PLX8SpMFVWB323y1wlLAVtQYVdiv34Wx1p",
             "https://www.youtube.com/watch?v=hTSg6S1h5V8&list=PLqAyA0PNRc0432DlzGam-sda-u4MzXCfg",
             "https://www.youtube.com/watch?v=cJw8FtPnAks&list=PLhw6V7H4ZhP5Y-xQ3SQJVrUMq8CfGIjtk",
             "https://www.youtube.com/watch?v=uUN12TouUrA&list=PLC1knAUAS7p4UjAwEmhJXSkUjGFqKC5mo",
             "https://www.youtube.com/watch?v=A8sFkwwf8Xk&list=PLmjz-onNqJyCgibMI-JfV7IqWyqaeMTyB",
             "https://www.youtube.com/watch?v=FCx5U-RsogQ&list=PL5oK2P-dW3oLNSf4Ltxqphxo-y3ZWGzoq",
             "https://www.youtube.com/watch?v=w7Wx1V9GNcs&list=PLpfrjHZTkRRAxv2L8sQ_Q7yh8HI7Fcz6d",
             "https://www.youtube.com/watch?v=ObhKOvPig74&list=PLtiSY73vW0ImROxDXWX78wtE4JI_VZm01",
             "https://www.youtube.com/watch?v=Jnt5nU-cqnY&list=PLmlj7LBy7MNbQXnIFH3JqQwKrw-r0Xdrl",
             "https://www.youtube.com/watch?v=3XRrxss6XIk&list=PLnFPnI83-2e8cQvTqOtHbmd05YS1L1ayJ",
             "https://www.youtube.com/watch?v=4Hv7ticWWKY&list=PL7E589AB8A32AF313",
             "https://www.youtube.com/watch?v=YyMlBhcGpSQ&list=PLYuhVRCyF1YucQzzB4gOkEyfL4Qjh7biS"]

save_path = 'C:\\Users\\lazar\\Desktop\\Songs'

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': save_path + '/%(playlist)s/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192'
    }],
    'noplaylist': False,
    'ffmpeg_location': 'C:\\ffmpeg\\bin'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for playlist in playlists:
        print(f"Downloading playlist: {playlist}")
        try:
            playlist_info = ydl.extract_info(playlist, download=True)
        except Exception as e:
            print(f"Error downloading song in playlist {playlist}: {e}")
            continue

        for video in playlist_info['entries']:
            try:
                video_url = video['url']
                print(f"Downloading video: {video_url}")
                ydl.download([video_url])
            except Exception as e:
                print(f"Error downloading video {video_url}: {e}")
                continue