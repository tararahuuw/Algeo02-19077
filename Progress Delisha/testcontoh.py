import io
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

file1 = open("filecontoh.txt")

factory = StemmerFactory()
stemmer = factory.create_stemmer()

sentence = file1.read()
stemsentence = stemmer.stem(sentence)

stopfactory = StopWordRemoverFactory()
stopword = stopfactory.create_stop_word_remover()
stopsentence = stopword.remove(stemsentence)

tokens = nltk.tokenize.word_tokenize(stopsentence)
kemunculan = nltk.FreqDist(tokens)
print(kemunculan.most_common())