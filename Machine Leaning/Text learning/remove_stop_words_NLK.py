import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

# nltk.download()
sw = stopwords.words("english")
print(len(sw))

# 词干提取
stemmer = SnowballStemmer("english")
print(stemmer.stem("absolution"))
