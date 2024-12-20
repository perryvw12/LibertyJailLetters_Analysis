import string
import re


def textparser(word_map, file_location):
    with open(file_location, "r", encoding="utf-8") as text:
            for line in text:
                words = line.split(" ")
                for word in words:
                    word = word.lower()
                    word = word.translate(str.maketrans("", "", string.punctuation))
                    word = re.sub(r'([a-z])\d+\b', r'\1', word)
                    if word in word_map:
                        word_map[word] += 1
                    else:
                        word_map[word] = 1
            return word_map