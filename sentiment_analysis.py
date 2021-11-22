punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(x):
    m = ''
    for c in x:
        if c not in punctuation_chars:
            m = m + c
    return m

def get_pos(x):
    c = 0
   
    word_str = strip_punctuation(x)
    word1 = word_str.lower()
    words = word1.split(' ')
    
    for wrd in words:
        if wrd in positive_words:
            c = c + 1
    return c

def get_neg(x):
    c = 0
   
    word_str = strip_punctuation(x)
    word1 = word_str.lower()
    words = word1.split(' ')
    
    for wrd in words:
        if wrd in negative_words:
            c = c + 1
    return c

twitter = open('project_twitter_data.csv', 'r')
  

twitter_text = []
for lin in twitter:
    
        twitter_text.append(lin.strip().split(','))
outfile = open('resulting_data.csv', 'w')
outfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
outfile.write('\n')

for tw in twitter_text:
    if tw != twitter_text[0]:
        pos_score = get_pos(tw[0])
        neg_score = get_neg(tw[0])
        net_score = pos_score - neg_score
        row_string = '{},{},{},{},{}'.format(tw[1],tw[2],pos_score,neg_score,net_score)
        outfile.write(row_string)
        outfile.write('\n')
    