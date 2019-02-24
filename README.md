## Python3.6-A quick text mining program on Twitter
- 本程式利用Tweepy API 搜尋近期20偏內包含seedword.txt檔案文字的Tweet，並做快速的文字分析

## 文字分析
- 基本架構，利用Textstat計算貼文的基本字詞數量(Char count,Syllabus count,Lexicon count,Sentence count)
- 可讀性(readability)，利用Textstat計算文本的易閱讀性高低(Gunning Fog Index、Flesch Reading Ease、Flesch-Kincaid Grade)
- 表情符號的計算與情感(emoji analysis)，計算表情符號出現的個數與情感分數，情感分數來源(http://kt.ijs.si/data/Emoji_sentiment_ranking/index.html)
- 文本情感分數(sentiment_score)，使用Textblob計算情感分數(Sentiment)與主觀性分數(Subjectivity)

## 註
- 注意發送request的時間不能過度頻繁，必要時配合sleep time調整
- 若想要一次搜尋超過20筆推文時，可調整include_entities=True,lang="en", tweet_mode='extended').items(20)中的參數(20)，調整時須參考 https://tweepy.readthedocs.io/en/v3.5.0/index.html
 
## 參考來源
1. Gunning Fog Index (FOG)
<br />McLaughlin, G. H. (1969).SMOG Grading-a New Readability Formula. Journal of Reading, 12(8), 639–646.
2. Flesch Reading Ease、Flesch-Kincaid Grade
<br />Kincaid, J. P., Aagard, J. A., O’Hara, J. W., &Cottrell, L. K. (1981).Computer readability editing system. IEEE Transactions on Professional Communication, PC-24(1), 38–42.
3. 表情符號情感 
<br />Novak, P. K., Smailović, J., Sluban, B., &Mozetič, I. (2015).Sentiment of emojis. PLoS ONE, 10(12), 1–22.

 ##
 - 使用語言：Python3.6
 - 主要套件：tweepy、textblob、regex、emoji、textstat
 
 若有任何問題，歡迎Email至 Lian555046@gmail.com
