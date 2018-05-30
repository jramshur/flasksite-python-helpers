# NOT IN USE YET. NEED TO EDIT WSGI.py file

from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/welcome')
    return render_template('welcome.html')

# Suggested by https://help.pythonanywhere.com/pages/Flask/.
# pythonanywhere can't run app.run directly, thus put it in the __main__ clause
if __name__ == '__main__':
    #db.create_all() # not sure if we need this, but it was in the example in the link above
    if 'liveconsole' not in gethostname():
        app.run()
