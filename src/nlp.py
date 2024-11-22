import sys
import nltk
import csv
from konlpy.tag import *
from re import match  # 전처리 위해서 정규표현식 관련 re 패키지 import

if __name__ == '__main__':
    # argument로 문장 받아오기
    # sentence = sys.argv[1]

    # 2.txt파일 읽어오기 for teㄴt
    sentence = ''
    with open('test/sentence_text.txt', 'r', encoding='UTF8') as f:
        line = f.readline()
        while line != '':
            sentence += line
            line = f.readline()

    # print('-'*100)
    # print(f'{sentence}')      
    # print('-'*100)

    ## 영어
    nouns_en = []
    word_tokens = nltk.word_tokenize(sentence)
    tokens_pos = nltk.pos_tag(word_tokens)
    for word, pos in tokens_pos:
        if 'NN' in pos:
            if len(str(word)) >= 2 :
                nouns_en.append(word)

    # print('영어')
    # print(nouns_en)
    # print('-'*100)
    
    # 한글
    nouns_ko = []
    okt = Okt()
    for noun in okt.nouns(sentence) :
        # 단어 전처리 : 2음절 이상, 수사 제외
        if len(str(noun)) >= 2 and not(match('^[0-9]', noun)) :
            nouns_ko.append(noun)

    # print('한글')
    # print(nouns_ko)
    # print('-'*100)

    complement = list(set(nouns_en) - set(nouns_ko))
    nouns = nouns_ko + complement
    # print('+')
    # print(nouns)
    # print('-'*100)

    word_count = {} # 빈 set
    for noun in nouns :
        word_count[noun] = word_count.get(noun, 0) + 1
    
    print('-'*100)
    print(word_count)
    print('-'*100)

    with open('test/nlp.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for noun in word_count:
            writer.writerow([noun, word_count[noun]])
