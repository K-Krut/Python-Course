import re


class Text:
    def __init__(self, file):
        try:
            self._file = file
        except(EOFError, IOError, FileExistsError, FileNotFoundError):
            print('file error')
            exit(1)

    def words_counting(self):
        text = open(self._file, 'r')
        count_ = sum(len(list(filter(lambda x: x, re.split(r'[, \n]+', line)))) for line in text)
        text.close()
        return count_

    def characters_counting(self):
        try:
            text = open(self._file, 'r')
        except(EOFError, IOError, FileExistsError, FileNotFoundError):
            print('file error')
        count_ = sum(len(line) for line in text)
        text.close()
        return count_

    def sentence_counting(self):
        try:
            text = open(self._file, 'r')
        except(EOFError, IOError, FileExistsError, FileNotFoundError):
            print('file error')
        help_list = list(
            line.replace('!?', '.').replace('?!', '.').replace('...', '.').replace('?\n', '?').replace('.\n', '.') for
            line in text)
        count_ = sum(len(list(filter(lambda x: x != '', re.split(r'[.!?]', line)))) for line in help_list)
        text.close()
        return count_

    def __str__(self):
        return f'Sentences: {text.sentence_counting()}, Words: {text.words_counting()}, Characters: {text.characters_counting()}'


try:
    text = Text('Task_2.txt')
    print(text)
except UnboundLocalError:
    exit()




# try:
#     text = open(self._file, 'r')
# except(EOFError, IOError, FileExistsError, FileNotFoundError):
#     print('file error')
# for line in text:
#     count_ = len(list(filter(lambda x: x, re.split(r"[, \n]+", line))))
# # count_ = sum(len(re.split('[ ,]', line)) for line in text)
# # count_ = sum(len(line.split()) for line in text)
# text.close()
# return f'Words: {count_}'


# count_ = len(list(filter(lambda x: x in ('. ', '.\n', '?', '?\n', '...', '!', '.', '!?'), line) for line in text))
# count_ = len(list(filter(lambda x: x, re.split(r'[.!?]+', line)) for line in text))
# count_ = list(re.split(r'[.!?]', line) for line in text)
# count_ = sum(len(list(filter(lambda x: x != '', re.split(r'[.!?]+', line)))) for line in text)
# count_ = sum(len(list(filter(lambda x: x != '', re.split('[.!?]', line.replace('?!', '.'))))) for line in text)