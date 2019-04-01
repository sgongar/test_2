#!/usr/bin/env python
# -*- coding: utf-8 -*-

import flask
from flask import request, jsonify

from prepare_dataframe import extract_df_restaurants

app = flask.Flask(__name__)
app.config["DEBUG"] = True

books = [
    {'lon': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'lon': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'lon': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@app.route('/restaurants/near/', methods=['GET'])
def near():
    lat = request.args.get('lat')
    lon = request.args.get('lon')

    df = extract_df_restaurants(cuisine='all', wheelchair=False)
    print(df)

    return(books)

app.run()
