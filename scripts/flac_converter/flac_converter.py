import os
from pathlib import Path

opus_cmd = 'ffmpeg -i "{file_name}" -c:a libopus -map_metadata 0 -id3v2_version 3 -b:a 128k ./opus/"{output_name}".opus'
mp3_cmd = 'ffmpeg -i "{file_name}" -ab 320k -map_metadata 0 -id3v2_version 3 ./mp3/"{output_name}".mp3'

for d in ('mp3', 'opus'):
    os.mkdir(d)

for f in [x for x in os.listdir() if os.path.isfile(x) if '.flac' in x]:
    output_name = Path(f).stem
    os.system(opus_cmd.format(file_name=f, output_name=output_name))
    os.system(mp3_cmd.format(file_name=f, output_name=output_name))
