yt-dlp --write-auto-subs --sub-format srt --skip-download \
       -P srt -o "%(playlist_index)s - %(title)s.%(ext)s" \
       "https://www.youtube.com/playlist?list=PLCTi8nkE1YPeFK31pbc1lmYiPvJNYMWL8"
