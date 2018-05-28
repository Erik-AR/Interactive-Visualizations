# import necessary libraries
import numpy as np

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################
dbfile = os.path.joinn('db', 'belly_button_biodiversity.sqlite')
engine = create_engine(f"sqlite:///{dbfile}")

Base = automap_base()

Base.prepare(engine, reflect=True)

Samples_Metadata = Base.classes.Samples_Metadata
OTU = Base.classes.otu
Samples = Base.classes.samples

Session = Session(engine)



# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")



# List of Names
@app.route('/names')
class BellyButton(db.Names):
    __tablename__ = 'belly_button_biodiversity'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    type = db.Column(db.String)
    age = db.Column(db.Integer)

    def __repr__(self):
        return '<bb %r>' % (self.name)



@app.route('/otu')



@app.route('/metadata/<sample>')



@app.route('/samples/<sample>')

@app.before_first_request
def setup():
    # Recreate database each time for demo
    db.drop_all()
    db.create_all()
