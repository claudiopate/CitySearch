from datetime import datetime
from elasticsearch import Elasticsearch, helpers

def write_doc_to_elasticsearch(list_cities):
    es = Elasticsearch()

    print("Writing " + str(len(list_cities)))
    if "Codice Comune formato alfanumerico" in list_cities[0]:
        actions = [
            {
                "_index": "cities",
                "_id": city["Codice Comune formato alfanumerico"],
                "_source": city
            } for city in list_cities
        ]
    elif "Codice Comune" in list_cities[0]:
        actions = [
            {
                "_index": "cities",
                "_id": city["Codice Comune"],
                "_source": city
            } for city in list_cities
        ]

    resp = helpers.bulk(es, actions)
    return resp


