import yt_dlp
import sys
import os


def get_user_inputs():
    channel_url = input("Enter Channel URL: ").strip()

    # Auto-append /shorts if missing
    if "/shorts" not in channel_url:
        if channel_url.endswith("/"):
            channel_url += "shorts"
        else:
            channel_url += "/shorts"

    print("\nChoose Sort Mode:")
    print("1. Newest")
    print("2. Most Popular")
    sort_choice = input("Enter choice (1 or 2): ").strip()

    try:
        limit = int(input("How many videos to download?: ").strip())
    except ValueError:
        print("Invalid number.")
        sys.exit(1)

    return channel_url, sort_choice, limit


def get_base_ydl_options(channel_name=None):
    outtmpl = '%(title)s.%(ext)s'

    if channel_name:
        outtmpl = f'{channel_name}/%(title)s.%(ext)s'

    return {
        'retries': float('inf'),
        'fragment_retries': float('inf'),
        'socket_timeout': 15,
        'force_ipv4': True,
        'format': 'best[height<=720][ext=mp4]/best[ext=mp4]/best',
        'merge_output_format': 'mp4',
        'outtmpl': outtmpl,
        'quiet': False
    }


def fetch_video_entries(channel_url):
    ydl_opts = get_base_ydl_options()
    ydl_opts.update({
        'extract_flat': True,
        'skip_download': True
    })

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(channel_url, download=False)

    if 'entries' not in info:
        print("No videos found.")
        sys.exit(1)

    return list(info['entries'])


def download_videos(video_list, channel_name):
    # Create folder if not exists
    os.makedirs(channel_name, exist_ok=True)

    ydl_opts = get_base_ydl_options(channel_name)

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for video in video_list:
            video_url = f"https://www.youtube.com/watch?v={video['id']}"
            print(f"\nDownloading: {video.get('title', video['id'])}")
            ydl.download([video_url])


def main():
    channel_url, sort_choice, limit = get_user_inputs()

    print("\nFetching video list...")
    entries = fetch_video_entries(channel_url)
    entries = [e for e in entries if e]

    if not entries:
        print("No videos found.")
        sys.exit(1)

    # Get channel name and clean invalid characters
    channel_name = entries[0].get('channel', 'Channel')
    channel_name = "".join(c for c in channel_name if c not in r'\/:*?"<>|')

    if sort_choice == "2":
        print("Sorting by Most Popular...")

        full_entries = []
        ydl_opts = get_base_ydl_options()
        ydl_opts.update({'skip_download': True})

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            for entry in entries:
                try:
                    video_url = f"https://www.youtube.com/watch?v={entry['id']}"
                    info = ydl.extract_info(video_url, download=False)
                    full_entries.append(info)
                except:
                    continue

        full_entries.sort(
            key=lambda x: x.get('view_count', 0),
            reverse=True
        )

        selected_videos = full_entries[:limit]

    else:
        print("Downloading Newest videos...")
        selected_videos = entries[:limit]

    print(f"\nStarting download of {len(selected_videos)} videos...")
    download_videos(selected_videos, channel_name)


if __name__ == "__main__":
    main()
