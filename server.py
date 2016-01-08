from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'my_secret_key'

# root -> load template
#session variables needed: 'gold!' <-- int, 'activites!' <-- list with dictionaries inside!
# post/get allow us to determine which type of building we went to
@app.route('/') # app.route('/', methods = ['GET'])
def initialize_page():
    try:
        session['gold'] #if this doesn't exist go to except.
        session['activities'] #if this doesn't exist go to except.
    except:
        session['gold'] = 0
        session['activities'] = []
    return render_template('index.html') #will be found in our templates folder

@app.route('/process_gold/<building>') # is a get!
def process_gold(building):
    mybuildings = {'farm': random.randrange(5,11), 'casino': random.randrange(-50,51), 'house': random.randrange(0,6), 'cave': random.randrange(15,26)}
    gold = mybuildings[building]
    session['gold'] += gold
    classtype = ('green','red')[gold <= 0]
    behaviour = ('gained','lost')[gold <= 0]
    session['activities'].append({'classtype':classtype,'text':'You visited the {}, and {} {}'.format(building, behaviour, str(gold))})
    return redirect('/')

# Temporary reset route
@app.route('/reset', methods = ['POST', 'DELETE'])
def remove_sessions():
    session.pop('gold')
    session.pop('activities')
    #session.clear()
    return redirect('/')


if __name__ == '__main__':
  app.run(debug = True)
