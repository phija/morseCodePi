import RPi.GPIO as GPIO
import time
from threading import Thread
 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)

alphabet = [['a',""],['b',""],['c',""],['o','lll'],['s','kkk']]


class Alphabet(object):
    
    def __init__(self):
        self._data = ''
        self._map = {}

    def create_map(self):
        for letter in self._data['alphabet']:
            self._map[letter['id']] = letter['code']

    def from_json(self):
        import json
        self._data = json.loads('{"alphabet":[\
                                 {"id":"a","code":".-"},\
                                 {"id":"b","code":"-..."},\
                                 {"id":"c","code":"-.-."},\
                                 {"id":"d","code":"-.."},\
                                 {"id":"e","code":"."},\
                                 {"id":"f","code":"..-."},\
                                 {"id":"g","code":"--."},\
                                 {"id":"h","code":"...."},\
                                 {"id":"i","code":".."},\
                                 {"id":"j","code":".---"},\
                                 {"id":"k","code":"-.-"},\
                                 {"id":"l","code":".-.."},\
                                 {"id":"m","code":"--"},\
                                 {"id":"n","code":"-."},\
                                 {"id":"o","code":"---"},\
                                 {"id":"p","code":".--."},\
                                 {"id":"q","code":"--.-"},\
                                 {"id":"r","code":".-."},\
                                 {"id":"s","code":"..."},\
                                 {"id":"t","code":"-"},\
                                 {"id":"u","code":"..-"},\
                                 {"id":"v","code":"...-"},\
                                 {"id":"w","code":".--"},\
                                 {"id":"x","code":"-..-"},\
                                 {"id":"y","code":"-.--"},\
                                 {"id":"z","code":"--.."},\
                                 {"id":"0","code":"-----"},\
                                 {"id":"1","code":".----"},\
                                 {"id":"2","code":"..---"},\
                                 {"id":"3","code":"...--"},\
                                 {"id":"4","code":"....-"},\
                                 {"id":"5","code":"....."},\
                                 {"id":"6","code":"-...."},\
                                 {"id":"7","code":"--..."},\
                                 {"id":"8","code":"---.."},\
                                 {"id":"9","code":"----."},\
                                 {"id":".","code":".-.-.-"},\
                                 {"id":",","code":"--..--"},\
                                 {"id":"?","code":"..--.."},\
                                 {"id":"!","code":"..--.."},\
                                 {"id":" ","code":" "}]}')


alphabet = Alphabet()
alphabet.from_json()
alphabet.create_map()

state = True

dit = 0.08
dah = dit * 3

def switchOn(duration, gpioNo):
    if duration == " ":
        time.sleep(7 * dit)
    elif duration == "_":
        time.sleep(dah)
    else:
        GPIO.output(gpioNo, True)
        if duration == "-":
            time.sleep(dah)
        else:
            time.sleep(dit)
        GPIO.output(gpioNo, False)
        time.sleep(dit)

def showLetter(string, gpioNo, alphabet):
    code = ""
    for letter in string:
        code += alphabet._map[letter] + "_"
    print("string: " + string + "  code: " + code)
    for sign in code:
        switchOn(sign, gpioNo)

threads = []
threads.append(Thread(target=showLetter, args=("sos", 3, alphabet)))
threads.append(Thread(target=showLetter, args=("how are you?", 2, alphabet)))

for t in threads:
    t.start()

for t in threads:
    t.join()

#GPIO.output(3, False)
#GPIO.output(2, False)
