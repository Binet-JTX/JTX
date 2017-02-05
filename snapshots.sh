#!/bin/bash
for filename in videos/*.mp4; do
    echo "$filename"
    ffmpeg -ss 00:00:04 -i "$filename" -vframes 1 -q:v 2 "snapshots/$(basename "$filename" .mp4).jpg"
done
for filename in videos/*.mov; do
    echo "$filename"
    ffmpeg -ss 00:00:04 -i "$filename" -vframes 1 -q:v 2 "snapshots/$(basename "$filename" .mov).jpg"
done
