import re
import os, time
import sqlite3
from collections import Counter
from string import punctuation
from math import sqrt
import wolframalpha # Get from here: https://pypi.python.org/pypi/wolframalpha
import ssl
import string
import smtplib
import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
import random
import json
from html.parser import HTMLParser
import sys
import time


#Html stripper-outer used to format some responses received when online
class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

# A really poor way of doing things I know but it was just to test out an idea and I haven't updated it all yet
# Incoming lists - Remember they need to be in lower case
name = ['what is your name?', 'what are you called', 'what are you called?', 'what is your name', 'whats your name', 'whats your name?', "what's your name", "what's your name?"]
helpme = ['help', 'help.']
game = ['play a game', 'play with me', 'play game', 'hangman', 'hang man']
made = ['who made you?', 'who wrote you?', 'who wrote you', 'who made you', 'who created you?', 'who created you', 'when were you made?', 'when were you made', 'when were you born?', 'when were you born', 'when is your birthday?', 'when is your birthday', 'when is it your birthday?', 'when is it your birthday']
jez = ['who is jez whitworth?', 'who is jez whitworth', 'who is jez?', 'who is jez', 'tell me about jez', 'tell me about jez whitworth', 'jez whitworth', 'jez whitworth?']
swear = ['*** Enter you choice of swear words to be used by the swear filter here *****']
note = ['take note.', 'take note']
noteread = ['read note.', 'read note']
greetwoggle = ['hello woggle.', 'hi woggle.', 'hello woggle', 'hi woggle']
thanks = ['thanks.', 'thanks', 'thank you.', 'thank you', 'thnaks', 'thnaks.', 'thank', 'thank.']


# Outgoing lists - Remember they need to be in lower case
howdy = ['Hi.', 'Hello.', 'Hi there.', "Hello, it's nice to chat to you.", 'Howdy.', 'Greetings.']
thanksreply = ['No problem.', 'No worries.', "You're welcome.", 'My pleasure.']


# Wolfram Alpha credentials - needed for general knowledge questions when online 
appid = 'AH4WJ6-R8Y9JTGKJ7' # <--- Insert your free Wolfram Alpha token here - https://developer.wolframalpha.com/portal/apisignup.html
client = wolframalpha.Client(appid)
 
# Connection details for the conversation database. If there is no file present or the location is referenced
# incorrectly then a new blank conversation file will be produced automatically in the location you set below.
connection = sqlite3.connect('/home/pi/Desktop/Woggle/conversation.sqlite') # <--- Just reference the location of the conversation file here
cursor = connection.cursor()
 
try:
    # Create the table containing the words
    cursor.execute('''
        CREATE TABLE words (
            word TEXT UNIQUE
        )
    ''')
    # Create the table containing the sentences
    cursor.execute('''
        CREATE TABLE sentences (
            sentence TEXT UNIQUE,
            used INT NOT NULL DEFAULT 0
        )''')
    # Create association between weighted words and the next sentence
    cursor.execute('''
        CREATE TABLE associations (
            word_id INT NOT NULL,
            sentence_id INT NOT NULL,
            weight REAL NOT NULL)
    ''')
except:
    pass
 
def get_id(entityName, text):
    """Retrieve an entity's unique ID from the database, given its associated text.
    If the row is not already present, it is inserted.
    The entity can either be a sentence or a word."""
    tableName = entityName + 's'
    columnName = entityName
    cursor.execute('SELECT rowid FROM ' + tableName + ' WHERE ' + columnName + ' = ?', (text,))
    row = cursor.fetchone()
    if row:
        return row[0]
    else:
        cursor.execute('INSERT INTO ' + tableName + ' (' + columnName + ') VALUES (?)', (text,))
        return cursor.lastrowid
 
def get_words(text):
    """Retrieve the words present in a given string of text.
    The return value is a list of tuples where the first member is a lowercase word,
    and the second member the number of time it is present in the text."""
    wordsRegexpString = '(?:\w+|[' + re.escape(punctuation) + ']+)'
    wordsRegexp = re.compile(wordsRegexpString)
    wordsList = wordsRegexp.findall(text.lower())
    return list(Counter(wordsList).items())
 



B = '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n Woggle V1.2\n Online...'
print(B)
while True:
    # ask for user input; if a blank line, then exit
    H = input('> ').strip()
    HLower = H.lower()

    if H == '':
        print ("> Thanks for chatting.")
        time.sleep(1)
        os.system("sudo shutdown -h now")
        break
    # Wolframalpha
    question = H.lower() # Lowercase
    firstword = question.partition(' ')[0] # Gets first word
    if firstword in ['question', 'question:', 'question-']:
        query = question.split(' ',1)[1] # Removes first word
        res = client.query(query)
        if len(res.pods) > 0:
                texts = ""
                pod = res.pods[1]
                if pod.text:
                    texts = pod.text
                else:
                    texts = "I don't have an answer for that I'm afraid."
                texts = texts.encode('ascii', 'ignore')
                ab = string.replace (texts, "Wolfram|Alpha", "Woggle")
                print(ab)
        else:
                print ("> Hmmm, I'm really not sure. Let me Google that...")
                base = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&'
                query = urllib.parse.urlencode({'q' : question})
                response = urllib.request.urlopen(base + query).read()
                data = json.loads(response)
                bc = data['responseData']['results'][0]['content']
                googleanswer = strip_tags(bc)
                print(googleanswer)
    # End Wolframalpha
    elif HLower in swear:
                print ("> No bad language please.")
    elif HLower in note:
                notename = input("> Enter file name: ")
                notecontent = input("Contents > ")
                f = open(notename +".txt","w")
                f.write(notecontent)
                f.close()
    elif HLower in noteread:
                notename = input("> Enter file name to read: ")
                try:
                    f = open(notename +".txt","r")
                    print((f.readline()))
                    f.close()
                except:
                    pass
                    print ("> Sorry, I can't find a file of that name.")
    elif HLower in name:
                print ("> My name is Woggle.")
    elif HLower in made:
                print ("> I was activated on 1st January 2016 by my creator Jez Whitworth.")
    elif HLower in jez:
                print ("> Jez is a nice chap.")
    elif HLower in helpme:
                print ("\n> Help menu: \nOffline:\n\n1. Hangman - Start a game of hangman with Woggle.\n2. Take note - Create a note for Woggle to save.\n3. Read note - Get Woggle to relay previously saved notes.\n\nOnline:\n\nQuestion (followed by question): Ask Woggle any question.\n")
    elif HLower in greetwoggle:
                print(("> ") + (random.choice(howdy)))
    elif HLower in thanks:
                print(("> ") + (random.choice(thanksreply)))
    elif HLower in game:
                # Words to play in the game - Just keep adding as many as you would like.
                hangmanlist = ['Adult','Aeroplane','Air','Aircraft Carrier','Airforce','Airport','Album','Alphabet','Apple','Arm','Army','Baby','Baby','Backpack','Balloon','Banana','Bank','Barbecue','Bathroom','Bathtub','Bed','Bed','Bee','Bible','Bible','Bird','Bomb','Book','Boss','Bottle','Bowl','Box','Boy','Brain','Bridge','Butterfly','Button','Cappuccino','Car','Carpet','Carrot','Cave','Chair','Chief','Child','Chisel','Chocolates','Church','Church','Circle','Circus','Circus','Clock','Clown','Coffee','Comet','Compact Disc','Compass','Computer','Crystal','Cup','Cycle','Data Base','Desk','Diamond','Dress','Drill','Drink','Drum','Dung','Ears','Earth','Egg','Electricity','Elephant','Eraser','Explosive','Eyes','Family','Fan','Feather','Festival','Film','Finger','Fire','Floodlight','Flower','Foot','Fork','Freeway','Fruit','Fungus','Game','Garden','Gas','Gate','Gemstone','Girl','Gloves','God','Grapes','Guitar','Hammer','Hat','Hieroglyph'] 
                hangman = random.choice(hangmanlist)
                hangman = hangman.lower()
                print ("> Time to play hangman!")
                time.sleep(1)
                print ("> Start guessing...")
                time.sleep(0.5)
                word = hangman
                guesses = ''
                turns = 10
                while turns > 0:         
                    failed = 0             
                    for char in word:      
                        if char in guesses:    
                            print((char,))    
                        else:
                            print(("_",))   
                            failed += 1    
                    if failed == 0:        
                        print ("\n> You won. Well done.")  
                        break              
                    print()
                    guess = input("Guess a character:") 
                    guesses += guess                    
                    if guess not in word:  
                        turns -= 1        
                        print ("Wrong\n")    
                        print(("You have"), + turns, ('more guesses')) 
                        if turns == 0:           
                            print(("> You Lose. The answer was ") + hangman) 
    else:
        # Thanks to Mathieu Rodic for the below SQLite code. I tried various approaches but I found this simple
		# method online and it did the same job in far fewer lines of code.
        words = get_words(B)
        words_length = sum([n * len(word) for word, n in words])
        sentence_id = get_id('sentence', H)
        for word, n in words:
            word_id = get_id('word', word)
            weight = sqrt(n / float(words_length))
            cursor.execute('INSERT INTO associations VALUES (?, ?, ?)', (word_id, sentence_id, weight))
        connection.commit()
        # retrieve the most likely answer from the database
        cursor.execute('CREATE TEMPORARY TABLE results(sentence_id INT, sentence TEXT, weight REAL)')
        words = get_words(H)
        words_length = sum([n * len(word) for word, n in words])
        for word, n in words:
            weight = sqrt(n / float(words_length))
            cursor.execute('INSERT INTO results SELECT associations.sentence_id, sentences.sentence, ?*associations.weight/(4+sentences.used) FROM words INNER JOIN associations ON associations.word_id=words.rowid INNER JOIN sentences ON sentences.rowid=associations.sentence_id WHERE words.word=?', (weight, word,))
        # if matches were found, give the best one
        cursor.execute('SELECT sentence_id, sentence, SUM(weight) AS sum_weight FROM results GROUP BY sentence_id ORDER BY sum_weight DESC LIMIT 1')
        row = cursor.fetchone()
        cursor.execute('DROP TABLE results')
        # otherwise, just randomly pick one of the least used sentences
        if row is None:
            cursor.execute('SELECT rowid, sentence FROM sentences WHERE used = (SELECT MIN(used) FROM sentences) ORDER BY RANDOM() LIMIT 1')
            row = cursor.fetchone()

        # tell the database the sentence has been used once more, and prepare the sentence
        B = row[1]
        cursor.execute('UPDATE sentences SET used=used+1 WHERE rowid=?', (row[0],))
        print(('> ' + B))
        
        

        
