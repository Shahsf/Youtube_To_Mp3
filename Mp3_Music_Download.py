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
count = 0
if output == []:
    print("No Songs were picked (Enter Songs name in Text File)")
    quit()

else:

    for word in output:
        songname = word
        get_url = ssss.downloadssong(songname)
        mp3download(get_url)
