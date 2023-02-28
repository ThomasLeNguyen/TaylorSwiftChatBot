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
                    size = len(CORPUS['input'][x][salty_scale])
                    # print(size)
                    # print(type(CORPUS['input']))
                    # print(CORPUS['input'].keys())
                    # print(type(print(CORPUS['input'][x][salty_scale])))
                    print(response:=CORPUS['input'][x][salty_scale][random.randint(0,size-1)])
                    return response
                else:
                    print(response:=random.choice(CORPUS['misc corpus']))
                    return response

