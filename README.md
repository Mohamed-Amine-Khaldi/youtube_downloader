# YouTube Shorts Downloader

A Python script to easily download YouTube Shorts from a specific channel. It allows you to sort by **Newest** or **Most Popular** and limits the number of downloads to your preference.

## Features
- 🎥 **Auto-detection**: Automatically handles channel URLs to find the `/shorts` tab.
- 📂 **Organized**: Creates a folder with the channel's name for the downloaded videos.
- ⬇️ **Sorting Options**:
  1.  **Newest**: Downloads the latest uploaded shorts.
  2.  **Most Popular**: Scans the channel and downloads the most viewed shorts.

## Prerequisites

To run this script, you need **Python** installed on your system.

### 1. Install Python Dependencies
Open your terminal and install the required library:

```bash
pip install yt-dlp
