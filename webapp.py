#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

import flask
from flask import request, jsonify
from flask import render_template

from utils import haversine
from prepare_dataframe import extract_df_restaurants

"""
   Copyright 2019 Samuel Góngora García
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
:Author:
    Samuel Góngora García (s.gongoragarcia@gmail.com)
"""
__author__ = 's.gongoragarcia@gmail.com'


app = flask.Flask(__name__)
app.config["DEBUG"] = True


def create_dict(df, radious, elements):
    """

    @param df:
    @param lon:
    @param lat:

    @return data:
    """
    df = df[df['distance'] < radious]
    data = df.sort_values(by='distance', ascending=True)
    data = data.reset_index(drop=True)
    data = data.drop(list(range(elements, df['distance'].size)))

    return data


@app.route('/restaurants/near/')
def near():
    lat = request.args.get('lat', default=1, type=float)
    lon = request.args.get('lon', default=1, type=float)

    df = extract_df_restaurants(cuisine='all', wheelchair=False)
    df['distance'] = haversine(lat, lon, df['lat'].values, df['lon'].values)

    out_df = create_dict(df, radious=10.0, elements=10)

    print(out_df.to_json(orient='records'))

    # address = request.args.get('address', default='street', type=str)
    # print(address)

    return('test')


app.run()
