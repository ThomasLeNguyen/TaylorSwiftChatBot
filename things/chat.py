import json
from things.actors import actor
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import random

sia = SentimentIntensityAnalyzer()

CORPUS = {}
with open('chatbot_corpus.json', 'r') as myfile:
    CORPUS = json.loads(myfile.read())


class chat(actor):
    def __init__(self, phone_number):
        super().__init__(phone_number)
        self.score = 0

        self.salty_scale =  "MEDIUM"

    def get_output(self,msg_input):
        sent = sia.polarity_scores(msg_input)
        basetokenizedinput = nltk.word_tokenize(msg_input)
        tokenizedinput = []
        for y in basetokenizedinput:
            tokenizedinput.append(y.lower())

        if sent['neu'] > .3:
           self.salty_scale =  "MEDIUM"
        if sent['neg'] > .4:
            self.salty_scale =  "SALTY"
        if sent['pos'] > .6:
            self.salty_scale =  "SWEET"
        
        pos_tags =  nltk.pos_tag( nltk.word_tokenize(msg_input))
        msg = None
        print(tokenizedinput)


        for i in range (len(CORPUS['input'])):
            for x in tokenizedinput:
                if x in CORPUS['input']:
                    print([self.salty_scale])
                    size = len([self.salty_scale][0])
                    print(size)
                    if size != 1:
                        return random.choice([self.salty_scale][0][random.randint(0,size-1)])
                    else:
                        return random.choice([self.salty_scale][0][0])

  
                


       # if msg_input in CORPUS['input']:
        #    return random.choice(CORPUS['input'][msg_input][self.salty_scale])
        #else:
         #   msg = None
          #  for i in range( len(CORPUS[ 'misc corpus' ]) ):
           #     msg = random.choice( CORPUS[ 'misc corpus' ] )
            #    if msg not in self.prev_msgs:
             #       break

        if msg == None:
            return [ random.choice( CORPUS[ 'misc corpus' ] ) ]
        else:
            return [ msg ]

