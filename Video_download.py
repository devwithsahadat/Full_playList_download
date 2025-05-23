import os
import yt_dlp

def download_media(url, output_folder, download_type, is_playlist):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    ydl_opts = {
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'writethumbnail': False,
        'writeinfojson': False,
        'writesubtitles': False,
        'writeautomaticsub': False,
        'postprocessors': [],
        'quiet': False,
        'nooverwrites': True,
        'noplaylist': not is_playlist,  # Download playlist if True, else single video
    }

    if download_type == 'audio':
        ydl_opts['format'] = 'bestaudio/best'
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    else:  # video
        ydl_opts['format'] = 'bestvideo+bestaudio/best'
        ydl_opts['merge_output_format'] = 'mp4'

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print("🔽 Downloading...")
            ydl.download([url])
            print("✅ Download complete!")
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("Select download type:")
    print("1. Playlist")
    print("2. Single Video")
    choice = input("Enter 1 or 2: ").strip()
    if choice == '1':
        is_playlist = True
    elif choice == '2':
        is_playlist = False
    else:
        print("⚠️ Invalid choice. Exiting.")
        exit()

    url = input("🔗 Enter YouTube link: ").strip()
    if not url:
        print("⚠️ No URL provided!")
        exit()

    output_folder = input("📁 Enter output folder (default: current directory): ").strip()
    if not output_folder:
        output_folder = "."

    print("Select format:")
    print("1. MP3 (audio)")
    print("2. MP4 (video)")
    format_choice = input("Enter 1 or 2: ").strip()
    if format_choice == '1':
        download_type = 'audio'
    elif format_choice == '2':
        download_type = 'video'
    else:
        print("⚠️ Invalid format choice. Defaulting to video.")
        download_type = 'video'

    download_media(url, output_folder, download_type, is_playlist)
