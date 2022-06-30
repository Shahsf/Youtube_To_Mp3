
from mp3download import mp3download
import ssss
with open('C://Mp3_Music_Download//music.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        output = []
        for line in f:
            line = line.rstrip()
            output.append(line)
for word in output:
   songname = word
   get_url = ssss.downloadssong(songname)
   mp3download(get_url)






