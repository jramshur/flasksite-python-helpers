# Page info here: ???


################################
# IMPORTS #
################################
from flask import Flask, render_template, request
from flask.ext.uploads import UploadSet, configure_uploads, IMAGES  # imports for file uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
from flask_bootstrap import Bootstrap
import os

################################
# CONFIG/SETUP/INITIALIZE
################################
app = Flask(__name__)
Bootstrap(app)  # initialize flask-bootstrap. I'm only using it for wtf forms as I manually applied Bootstrap to my templates. Not sure if this will cause any complications/conflicts)

app.config[
    'UPLOADS_DEFAULT_TEST'] = os.getcwd() + "/mysite/uploads"  # destination folder for uploads. Must use standard syntaxt.
app.config['SECRET_KEY'] = 'I have a dream'

# Configure the image uploading via Flask-Uploads
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

################################
# FORMS #
################################
# config Flask-WTform
class UploadPhotoForm(FlaskForm):
    photo = FileField(validators=[FileAllowed(photos, u'Image only!'), FileRequired(u'File was empty!')])
    submit = SubmitField(u'Upload')


class UploadRISForm(FlaskForm):
    photo = FileField(validators=[FileAllowed(photos, u'Image only!'), FileRequired(u'File was empty!')])
    submit = SubmitField(u'Upload')


################################
# ROUTES #
################################
@app.route('/')
def fn_home():
    return render_template('home.html')


@app.route('/upload/', methods=['GET', 'POST'])
def fn_uploadphoto():
    form = UploadPhotoForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = photos.url(filename)
    else:
        file_url = None
    return render_template('upload.html', form=form, file_url=file_url)


@app.route('/sandbox/')
def fn_sandbox():
    return render_template('sandbox.html')


@app.route('/littools/')
def fn_littools():
    return render_template('littools.html')


@app.route('/littools/ris_convert/', methods=['GET', 'POST'])
def fn_risconvert():
    form = UploadRISForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = photos.url(filename)
    else:
        file_url = None

    # load python code file to display on page
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'functions/text.py')

    fh = open(my_file, 'r')
    codecontent = fh.read()

    return render_template('ris_convert.html',
                           form=form,
                           file_url=file_url,
                           content=codecontent)


# def hello_world():
#    return 'Hello world using Flask v0.1!'

# Suggested by https://help.pythonanywhere.com/pages/Flask/.
# pythonanywhere can't run app.run directly, thus put it in the __main__ clause
if __name__ == '__main__':
    # db.create_all() # not sure if we need this, but it was in the example in the link above
    # if 'liveconsole' not in gethostname():
    app.run(debug=true)
