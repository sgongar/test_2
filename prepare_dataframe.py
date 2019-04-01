#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import json


def create_synonyms_dictionary():
    """

    """

    synonyms_dict = {'afghanistan': ['afghan'],
                     'argentine': ['argentinisches', 'argentinian'],
                     'armenia': ['armenian', 'armenean'],
                     'australia': ['australian'],
                     'austria': ['austrian'],
                     'bosnia': ['bosnian'],
                     'brazil': ['brazilian'],
                     'china': ['chinese', 'cantonese', 'China'],
                     'cyprus': ['cyprian'],
                     'croatia': ['croatian'],
                     'cuba': ['cuban'],
                     'egypt': ['egyptian', 'egypt'],
                     'france': ['french'],
                     'georgia': ['georgie', 'georgian'],
                     'germany': ['deutsch', 'german', 'rhenish', 'sausage',
                                 'swabian', 'bavarian', 'thuringian', 'Weine',
                                 'altbayerisch', 'regional'],
                     'greece': ['greek'],
                     'hungary': ['hungarian'],
                     'india': ['indian', 'Indische', 'Indisch'],
                     'indonesia': ['indonesian', 'indonesia'],
                     'iran': ['persisch', 'iranian', 'persian'],
                     'israel': ['israeli'],
                     'italy': ['italian', 'Pizza', 'pizza', 'pasta'],
                     'jamaica': ['Jamaican'],
                     'japan': ['sushi', 'japanese', 'ramen', 'suhi'],
                     'korea': ['korean', 'koreanisch'],
                     'latvia': ['latvian'],
                     'macedonian': ['macedonian'],
                     'malaysia': ['malaysian'],
                     'mexico': ['mexican'],
                     'morocco': ['moroccan'],
                     'norway': ['norgewian'],
                     'philippines': ['filipino', 'philippinisch',
                                     'phillipinian'],
                     'poland': ['polish'],
                     'russia': ['russian'],
                     'singapore': ['singaporean', 'Singapuri', 'singapore'],
                     'slovak_slow_food': ['slovak_slow_food'],
                     'syria': ['syrian'],
                     'spain': ['spanish', 'tapas'],
                     'sudan': ['sudanese'],
                     'switzerland': ['swiss'],
                     'taiwan': ['taiwanese'],
                     'thailand': ['thai'],
                     'turkey': ['turkish', 'kebab'],
                     'ukraine': ['ukrainian'],
                     'uzbekistan': ['uzbek'],
                     'vietnam': ['vietnamese', 'Vietnamesische', 'vietnam',
                                 'viet-food', 'viet'],
                     'arab': ['Arab', 'arab', 'arabic', 'arabisch'],
                     'nepal': ['nepalese', 'nepal', 'nepali'],
                     'yugoslavia': ['yugoslavian'],
                     'lebanon': ['libanese', 'lebanese'],
                     'caribbean': ['caribbean'],
                     'trinidad': ['trinidad'],
                     'jewish': ['jewish'],
                     'pakistan': ['pakistani'],
                     'peru': ['peruvian'],
                     'tibet': ['tibetan'],
                     'laos': ['laotian', 'laos'],
                     'indochina': ['indochinese'],
                     'portugal': ['portuguese'],
                     'catalonia': ['catalan'],
                     'bulgaria': ['bulgarien', 'bulgarian'],
                     'africa': ['Afrikanisches', 'african'],
                     'anatolia': ['anatolian'],
                     'asia': ['asian'],
                     'balkan': ['balkan'],
                     'mediterranean': ['mediterranean'],
                     'scandinavia': ['scandinavian'],
                     'hawaii': ['Hawaiian', 'hawaiian'],
                     'veggie': ['vegetarian', 'vegan'],
                     'soup': ['soup', 'soups'],
                     'steak': ['steak', 'steak_house'],
                     'seafood': ['seafood'],
                     'breakfast': ['breakfast'],
                     'coffee': ['coffee_shop', 'cafe'],
                     'bbq': ['bbq', 'barbacue'],
                     'potato': ['potato'],
                     'latin': ['latin-american', 'latin_american',
                               'lateinamerikanische'],
                     'salad': ['salad', 'salads'],
                     'bagel': ['bagel'],
                     'burger': ['burger'],
                     'canteen': ['canteen'],
                     'chicken': ['chicken'],
                     'fastfood': ['fastfood'],
                     'gourmet': ['gourmet'],
                     'hummus': ['hummus'],
                     'ice_cream': ['ice_cream'],
                     'international': ['international'],
                     'lunch': ['lunch'],
                     'pubfood': ['pubfood'],
                     'other': ['other'],
                     'oriental': ['oriental'],
                     'sandwich': ['sandwich'],
                     'southern_states': ['southern_states'],
                     'alpine_hut': ['alpine_hut'],
                     'modern_european_cusine': ['modern_european_cusine'],
                     'crepe': ['crepe'],
                     'fine_dining': ['fine_dining'],
                     'New_London_Cuisine': ['New_London_Cuisine'],
                     'frites': ['frites'],
                     'soul_food': ['soul_food'],
                     'fondue': ['fondue'],
                     'Dumplings': ['Dumplings'],
                     'wine_tavern': ['wine_tavern'],
                     'ayurvedisch': ['ayurvedisch'],
                     'bierverkostung': ['bierverkostung'],
                     'casual_fine_dining': ['casual_fine_dining'],
                     'verschieden': ['verschieden'],
                     'fish': ['fish']}

    with open('synonyms.json', 'w') as fp:
        json.dump(synonyms_dict, fp, sort_keys=True, indent=4)


def categorise_cuisine(cuisine):
    """
    """
    tags = []

    with open('synonyms.json', 'r') as fp:
        synonyms_dict = json.load(fp)

    for key_ in synonyms_dict.keys():
        for synonym in synonyms_dict[key_]:
            if synonym in cuisine:
                tags.append(key_)

    tags = list(set(tags))

    return tags


def create_dict(keys_list):
    """ Creates a dictionary from a given list of keys """
    dict_ = {}
    for key_ in keys_list:
        dict_[key_] = []

    return dict_


def extract_df_restaurants(cuisine, wheelchair):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """
    restaurants_df = pd.read_json('datasets/berlin_restaurants.json',
                                  orient='records')
    tags = restaurants_df['tags']

    tags_dict = create_dict(['amenity', 'cuisine', 'toilets:wheelchair',
                             'wheelchair', 'opening_hours'])

    for row in tags:
        for tag in tags_dict:
            if tag in row.keys():
                if tag is 'cuisine':
                    tags_dict[tag].append(categorise_cuisine(row[tag]))
                else:
                    tags_dict[tag].append(row[tag])
            else:
                tags_dict[tag].append([])

    # Categorise cuisine
    bool_cuisine_list = []
    for tags_cuisine in tags_dict['cuisine']:
        if cuisine is not 'all':
            if cuisine in tags_cuisine:  # Checks if is our cuisine
                bool_cuisine_list.append(True)
            else:  # If not rejects the restaurant
                bool_cuisine_list.append(False)
        else:
            bool_cuisine_list.append(True)

    # Categorise wheelchair
    bool_wheelchair_list = []
    for tag_wheelchair in tags_dict['wheelchair']:
        if tag_wheelchair == 'yes':
            bool_wheelchair_list.append(True)
        else:
            bool_wheelchair_list.append(False)

    # Create Series
    amenity_series = pd.Series(tags_dict['amenity'], name='amenity')
    cuisine_series = pd.Series(tags_dict['cuisine'], name='cuisine')
    bool_cuisine_series = pd.Series(bool_cuisine_list, name='cuisine_bool')
    toilets_wheelchair_series = pd.Series(tags_dict['toilets:wheelchair'],
                                          name='toilets:wheelchair')
    wheelchair_series = pd.Series(tags_dict['wheelchair'], name='wheelchair')
    bool_wheelchair_list = pd.Series(bool_wheelchair_list,
                                     name='wheelchair_bool')
    opening_hours_series = pd.Series(tags_dict['opening_hours'],
                                     name='opening_hours')

    restaurants_df = pd.concat([restaurants_df['id'], restaurants_df['lat'],
                                restaurants_df['lon'], amenity_series,
                                cuisine_series, bool_cuisine_series,
                                toilets_wheelchair_series,
                                wheelchair_series, bool_wheelchair_list,
                                opening_hours_series],
                               axis=1)

    # Filter by cuisine
    restaurants_df = restaurants_df[restaurants_df['cuisine_bool']]

    # Filter by wheelchair
    if wheelchair:
        restaurants_df = restaurants_df[restaurants_df['wheelchair_bool']]

    return restaurants_df
