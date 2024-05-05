import csv
from youtube_transcript_api import YouTubeTranscriptApi 

# assigning srt variable with the list 
# of dictionaries obtained by the get_transcript() function
url = "https://www.youtube.com/watch?v=UF8uR6Z6KLc"
length = 0
text = []
for i in range(len(url)-1, -1, -1):
    if url[i] == '=':
        break
    length += 1
url = url[len(url)-length:]
srt = YouTubeTranscriptApi.get_transcript(url, languages=['ko', 'en'])

# prints the result
for i in srt:
    text.append(i['text'])

file = open('myfile.txt', 'w')
for i in text:
    file.write(i)
    file.write(' ')
file.close()
# if the same file does exist, i want to delete and create new version again.
