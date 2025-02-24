# Youtube Video Downloader

This project is a Python script that allows you to download videos from youtube in different qualities. It uses the `yt-dlp` library to perform the download and `tqdm` to display a progress bar during the process.

## Features
- Video Donwload: Downloads YouTube videos in different resolutions.
- Quality Selection: Allows users to select their desired quality before starting the download.
- Progress Bar: Displays a strylized progress bar during download.
- Custom Directory: Allows saving video to a specific folder or the current directory.

## Requirements
- Python 3.6+
- Libraries: `yt-dlp`, `tqdm`

## Installation
- Clone the repository: `git clone git@github.com:Math7usFilipe/yt_video_downloader.git`
- Install the dependencies: `pip install yt-dlp tqdm`
- Exeecute the script: `python yt_video_downloader.py`

## How to Use
- Execute the script: `python yt_video_downloader.py`
- Enter the name of the folder where you want to save the video (or leave it blank to save in the current directory).
- Enter the URL of the YouTube video you want to download.
- Select the desired quality of the video.
- wait for the download to complete.

## Use example

```
=== YouTube Video Downloader ===

Enter the folder name to save the video (leave blank for current folder): videos
Enter the YouTube video URL: https://www.youtube.com/watch?v=example

Fetching video info...

Available qualities:
1. 1080p (Format: 137)
2. 720p (Format: 136)
3. 480p (Format: 135)
Enter the desired quality number: 2

Starting download...
Downloading: 100%|████████████████████| 150M/150M [00:30<00:00, 5.0MB/s]

Download complete! Video saved in: videos
```