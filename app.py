# import necessary libraries
import numpy as np
import os
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
db= os.path.join('db', 'belly_button_biodiversity.sqlite')
engine = create_engine(f"sqlite:///{db}")

Base = automap_base()

Base.prepare(engine, reflect=True)

Samples_Metadata = Base.classes.samples_metadata
OTU = Base.classes.otu
Samples = Base.classes.samples

Session = Session(engine)



# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")



# List of Names
@app.route('/names')
class BellyButton(db.names):
    __tablename__ = 'belly_button_biodiversity'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    type = db.Column(db.String)
    age = db.Column(db.Integer)

    def __repr__(self):
        return '<bb %r>' % (self.name)



@app.route('/otu')

    results = session.query(OTU.lowest_taxonomic_unit_found).all()
    otu_list = list(np.ravel(results))
    return jsonify(otu_list)

@app.route('/metadata/<sample>')
def sample_metadata(sample):
    sel = [Samples_Metadata.SAMPLEID, Samples_Metadata.ETHNICITY,
           Samples_Metadata.GENDER, Samples_Metadata.AGE,
           Samples_Metadata.LOCATION, Samples_Metadata.BBTYPE]


@app.route('/samples/<sample>')
    stmt = session.query(Samples).statement
    df = pd.read_sql_query(stmt, session.bind)
    if sample not in df.columns:
        return jsonify(f"Error! Sample: {sample} Not Found!"), 400


    data = [{
        "otu_ids": df[sample].index.values.tolist(),
        "sample_values": df[sample].values.tolist()
    }]
    return jsonify(data)
@app.before_first_request
def setup():
    # Recreate database each time for demo
    db.drop_all()
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)