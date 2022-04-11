
from string import punctuation

from numpy import take
import wordcloud


freq = {}
alloted = []
for l in punctuations:
    file_contents = file_contents.replace(letter , '')
for words in unintereting_words:
    w = ' ' + words + ' '
    file_contents = file_contents.replace(w , ' ')
for word in file_contents.split():
    if word.lower not in alloted:
        alloted.append(word.lower())
    if word not in freq:
        freq[word] = 1
    else:
        freq[word] += 1


cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(freq)
return cloud.to_image()   