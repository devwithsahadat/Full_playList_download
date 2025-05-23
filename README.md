<!-- Banner Icon -->
<p align="center">
  <img src="https://img.icons8.com/color/96/000000/youtube-play.png" alt="YouTube Icon" width="96" height="96"/>
</p>

# YouTube Playlist & Video Downloader

A simple, terminal-based tool to download entire YouTube playlists or single videos as MP3 (audio) or MP4 (video) files. Powered by [yt-dlp](https://github.com/yt-dlp/yt-dlp) for fast and reliable downloads.

---

## ✨ Features
- Download **entire playlists** or **single videos**
- Choose between **MP3 (audio)** or **MP4 (video)** output
- Save downloads to any folder of your choice
- Clean output: only one file per video/audio, no extra clutter
- Simple, interactive terminal prompts

---

## 🚀 Installation

1. **Clone this repository or download `yt.py`**
2. **Install Python 3.x** (if not already installed)
3. **Install dependencies:**
   ```sh
   pip install yt-dlp
   ```
4. **(Optional) Install FFmpeg** for best audio/video conversion
   - [FFmpeg Download](https://ffmpeg.org/download.html)
   - Make sure FFmpeg is in your system PATH

---

## 🛠️ Usage

1. Open your terminal and navigate to the folder containing `yt.py`.
2. Run the script:
   ```sh
   python yt.py
   ```
3. Follow the prompts:
   - Select download type: `1` for Playlist, `2` for Single Video
   - Enter the YouTube link (playlist or video URL)
   - Enter the output folder (or press Enter for current directory)
   - Select format: `1` for MP3 (audio), `2` for MP4 (video)

---

## 📦 Example
```
Select download type:
1. Playlist
2. Single Video
Enter 1 or 2: 2
🔗 Enter YouTube link: https://www.youtube.com/watch?v=example
📁 Enter output folder (default: current directory): downloads
Select format:
1. MP3 (audio)
2. MP4 (video)
Enter 1 or 2: 1
🔽 Downloading...
✅ Download complete!
```

---

## 📝 Notes
- Only one output file per video/audio will be created (no extra files)
- `.part` files are temporary and should disappear after the download finishes
- For playlists, all videos will be downloaded in the selected format

---

## 🛠️ Troubleshooting
- **No output file?** Check your internet connection and make sure the URL is correct
- **FFmpeg errors?** Install FFmpeg and ensure it is in your system PATH
- **Permission errors?** Make sure you have write access to the output folder

---

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <b>Enjoy downloading your favorite YouTube content!</b>
</p> 
