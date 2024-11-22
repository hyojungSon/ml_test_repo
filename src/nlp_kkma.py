import sys
import csv
from konlpy.tag import Kkma
from re import match  # 전처리 위해서 정규표현식 관련 re 패키지 import

if __name__ == '__main__':
    # sentence = sys.argv[1]
    sentence = ''
    file = open('D:\workspace\python_project\sentence_text.txt', 'r', encoding='UTF8')
    sentence = file.read()
    file.close()

    kkma = Kkma()
    nouns = []
    ex_sent = kkma.sentences(sentence)
    ex_nouns = kkma.nouns(sentence)
    for sent in ex_nouns :
        for noun in kkma.nouns(sent) :
            # 단어 전처리 : 2음절 이상, 수사 제외
            if len(str(noun)) >= 2 and not(match('^[0-9]', noun)) :
                nouns.append(noun)

    word_count = {} # 빈 set
    for noun in nouns :
        word_count[noun] = word_count.get(noun, 0) + 1

    with open('nlp_list.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        for noun in word_count:
            writer.writerow([noun, word_count[noun]])
