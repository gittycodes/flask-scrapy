from flask import render_template
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import threading
from miggr.website.new.new.spiders.contentspider import start_crawling

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

########### Forms ############
##############################


class InputMerchant(FlaskForm):
    website = StringField('Enter Website', validators=[DataRequired()])
    mid = StringField('MID')
    submit = SubmitField('Start Scan')


########### App ##############
##############################


@app.route('/', methods=['GET', 'POST'])
def home():
    website_form = InputMerchant()

    if website_form.validate_on_submit():

        website = website_form.website.data
        mid = website_form.mid.data

        execute_thread = threading.Thread(target=start_crawling, args=(website,), daemon=True)
        execute_thread.start()

        return render_template('home.html', website_form=website_form)

    return render_template('home.html', website_form=website_form)


if __name__ == '__main__':
    app.run(debug=True)
