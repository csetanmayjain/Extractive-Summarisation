from sklearn.feature_extraction.text import TfidfVectorizer
from nltk import tokenize
a=open("025.txt")
data=a.read()
data=data.replace('\n',' ')
line= tokenize.sent_tokenize(data)
tfidf=TfidfVectorizer()
len_data=len(line)
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
x=[]
for i in line: 
 example_sent =i
 stop_words = set(stopwords.words('english'))
 word_tokens = word_tokenize(example_sent)
 filtered_sentence = [w for w in word_tokens if not w in stop_words]
 filtered_sentence = []
 for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w) 
 z=filtered_sentence
 z=str(z)
 z=z.replace(","," ")
 z=z.replace("'"," ")
 z=z.replace("  "," ")
 x.append(z)
x=tfidf.fit_transform(x)
x=x.todense()
sent=[]
for j in range (0,(x.shape[0])):
 summ=0
 for k in range (0,(x.shape[1])):
   summ+=x.item((j,k))
 sent.append(summ)
c=[]
length=len(line)
for i in range(0,length):
    m=[]
    m.append(line[i])
    m.append(sent[i])
    c.append(m)
for j in range(0,length-1):
 for i in range (0,length-1):
    if(c[i][1]<c[i+1][1]):
        temp=c[i]
        c[i]=c[i+1]
        c[i+1]=temp 
num=input("Enter Number of lines of summary you want:- ")
for i in range (0,int(num)):
    print(c[i][0])