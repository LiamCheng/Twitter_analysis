import emoji
import regex
import re, string
from textstat.textstat import textstat
from textblob import TextBlob

def set_emojitable():
    file = 'EmojiSentiment.csv'
    emojilist = []
    emojisent = []
    with open(file) as inFile:
        for emoji in inFile.readlines():
            emoji = emoji.split(',')
            emojilist.append(emoji[1])
            emojisent.append(emoji[7])
    emoji_table = dict(zip(emojilist, emojisent))
    return emoji_table

def composition(text,file):
    char_count = textstat.char_count(text)
    syll_count = textstat.syllable_count(text)
    lex_count = textstat.lexicon_count(text)
    sent_count = textstat.sentence_count(text)
    file.write('\nChar count : %d\nSyllabus count : %d \nLexicon count : %d \nSentence count : %d' % (char_count, syll_count, lex_count,
            sent_count))

def readability(text,file):
    fog = textstat.gunning_fog(text)
    fres = textstat.flesch_reading_ease(text)
    fkgl = textstat.flesch_kincaid_grade(text)
    file.write('\nGunning Fog Index: %d \nFlesch Reading Ease: %d \nFlesch-Kincaid Grade: %d'% (fog, fres, fkgl))

def emojianalysis(text,file):
    emoji_table = set_emojitable()
    emoji_counter = 0
    data = regex.findall(r'\X', text)
    score = 0
    for word in data:
        if any(char in emoji.UNICODE_EMOJI for char in word):
            emoji_counter += 1
            emojiuni = str(word.encode('unicode_escape'))
            emojiuni = re.sub('[%s]' % re.escape(string.punctuation), '', emojiuni)
            emojiuni = emojiuni.replace('bU000', '0x')
            if emojiuni in emoji_table:
                score = score + float(emoji_table[emojiuni])
            text = text.replace(word, '')

    if emoji_counter > 0:
        score = score / emoji_counter

    file.write("\nEmoji counter: %d\nEmoji score: %s"%( emoji_counter, score))

def sentiment_score(text,file):
    text = TextBlob(text)
    sent = text.sentiment.polarity
    subj = text.sentiment.subjectivity
    file.write("\nSentiment score : %f \nSubjectivity score : %s \n---------\n"%( sent, subj))


def info(id,time,text,file):

    file.write("Tweet id : %s \nPost Time: %s \nText: %s" % (id ,time, text))
    composition(text,file)
    readability(text,file)
    emojianalysis(text,file)
    sentiment_score(text,file)
