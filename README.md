# YouTube Shorts Downloader

A Python automation tool that allows you to bulk download YouTube Shorts from any channel. You can filter by **Newest** or **Most Popular** uploads and specify exactly how many videos you want.

## 📋 Prerequisites

To run this tool, you need to have the following installed on your computer:

1.  **Python 3.x**
2.  **FFmpeg** (Crucial for merging video and audio)
    *   **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html), extract the folder, and add the `bin` folder to your system PATH.
    *   **Mac**: Run `brew install ffmpeg`
    *   **Linux**: Run `sudo apt install ffmpeg`

## 🛠️ Installation

1.  **Clone the repository** (or download the files):
    ```bash
    git clone https://github.com/Mohamed-Amine-Khaldi/youtube_downloader.git
    cd youtube_downloader
    ```

2.  **Install the required Python library**:
    ```bash
    pip install yt-dlp
    ```

## 🚀 How to Use

1.  Run the script in your terminal:
    ```bash
    python main.py
    ```
    *(Note: Replace `main.py` with the actual name of your python file if it is different)*

2.  **Follow the prompts**:
    *   Paste the **Channel URL** (e.g., `https://www.youtube.com/@ChannelName`).
    *   Choose a sorting method:
        *   `1`: Download the **Newest** videos.
        *   `2`: Download the **Most Popular** videos.
    *   Enter the **number of videos** to download.

The script will create a folder with the channel's name and save all MP4 files there.

## ⚠️ Disclaimer
This tool is for educational purposes only. Please respect YouTube's Terms of Service and the copyright of content creators.
