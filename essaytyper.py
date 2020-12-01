from flask import Flask
from flask import request
from wikiwriter import *
import random

app = Flask(__name__)

choose = open("/Users/asafyaellebovic/Desktop/Code/Nov 2020/JT/picker.html", "r").readlines()
choose = ' '.join([str(elem) for elem in choose])

animals = ["Dog","Cat","Horse","Camel","Squirrel", "Geoduck", "Glass_frog"]
people = ["Miyamoto_Musashi", "Binders_full_of_women","Albert_Einstein","Isaac_Newton","John_Lennon","Juan_Pujol_García"]
things = ["War_of_1812", "Emu_War", "Concorde", "Self-pollination","Trench_raiding_club", "Academic_dishonesty"]
places = ["France", "Italy", "Centralia,_Pennsylvania", "Pennsylvania_Station_(1910–1963)", "Monowi,_Nebraska", "Principality_of_Sealand"]

htmlcontents = '';

def dump(content):
    htmlcontents = open("/Users/asafyaellebovic/Desktop/Code/Nov 2020/JT/index.html", "r").readlines()
    htmlcontents = ' '.join([str(elem) for elem in htmlcontents])
    print(htmlcontents)
    htmlcontents = htmlcontents.replace("REPLACEME", "`"+str(wikiGet(content).replace('"',"ʻ").replace("'","ʻ"))+"`").replace("GETTITLE", '"'+content+'"')
    print(htmlcontents)
    return htmlcontents

@app.route('/')
def index():
  return choose

@app.route('/write', methods = ['GET'])
def writer():
    topic = request.args.get('topic', None)
    if topic == "animals":
        return dump(random.choice(animals))
    elif topic == "people":
        return dump(random.choice(people))
    elif topic == "places":
        return dump(random.choice(places))
    else:   
        return dump(random.choice(things))


if __name__ == '__main__':
    app.debug = True
    app.run() #go to http://localhost:5000/ to view the page.ll
