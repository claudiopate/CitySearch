from elasticsearch import Elasticsearch

es = Elasticsearch(hosts="http://es01:9200/")

def search(city):
    
    body_query = {
        "_source": ["Denominazione (Italiana e straniera)","Denominazione Comune","Codice Comune formato alfanumerico","Sigla automobilistica", "Comune soppresso per scorporo", "Codice Comune","Sigla Automobilistica"],
        "size": 10000,
        "query": {
            "bool": {
            "must": [],
            "filter": [
                {
                    "bool": {
                        "should": [
                        {
                            "bool": {
                            "should": [
                                {
                                "query_string": {
                                    "fields": [
                                    "Denominazione (Italiana e straniera)"
                                    ],
                                    "query": city
                                }
                                }
                            ],
                            "minimum_should_match": 1
                            }
                        },
                        {
                            "bool": {
                            "should": [
                                {
                                "query_string": {
                                    "fields": [
                                    "Denominazione Comune"
                                    ],
                                    "query": city
                                }
                                }
                            ],
                            "minimum_should_match": 1
                            }
                        }
                        ],
                        "minimum_should_match": 1
                    }
                }
            ],
            "should": [],
            "must_not": []
            }
        }
    }

    res = es.search(index="cities", doc_type="_doc", body=body_query)

    response = []

    for doc in res['hits']['hits']:
        item_city = {}
        print(doc)
        city_removed = False
        if "Comune soppresso per scorporo" in doc["_source"]:
            city_removed = True

        if city_removed:
            item_city = {
                "City_Name" : doc["_source"]['Denominazione Comune'],
                "City_Code": doc["_source"]['Codice Comune'],
                "Province_Code": doc["_source"]['Sigla Automobilistica'],
                "Suppressed": city_removed
            }
        else:
            item_city = {
                "City_Name" : doc["_source"]['Denominazione (Italiana e straniera)'],
                "City_Code": doc["_source"]['Codice Comune formato alfanumerico'],
                "Province_Code": doc["_source"]['Sigla automobilistica'],
                "Suppressed": city_removed
            }
        response.append(item_city)

    return response



def search_by_code(code):
    
    body_query = {
        "_source": ["Denominazione (Italiana e straniera)","Denominazione Comune","Codice Comune formato alfanumerico","Sigla automobilistica", "Comune soppresso per scorporo", "Codice Comune","Sigla Automobilistica"],
        "size": 10000,
        "query": {
            "bool": {
            "must": [],
            "filter": [
                {
                    "bool": {
                        "should": [
                        {
                            "bool": {
                            "should": [
                                {
                                "query_string": {
                                    "fields": [
                                    "Codice Comune formato alfanumerico"
                                    ],
                                    "query": code
                                }
                                }
                            ],
                            "minimum_should_match": 1
                            }
                        },
                        {
                            "bool": {
                            "should": [
                                {
                                "query_string": {
                                    "fields": [
                                    "Codice Comune"
                                    ],
                                    "query": code
                                }
                                }
                            ],
                            "minimum_should_match": 1
                            }
                        }
                        ],
                        "minimum_should_match": 1
                    }
                }
            ],
            "should": [],
            "must_not": []
            }
        }
    }

    res = es.search(index="cities", doc_type="_doc", body=body_query)

    response = []

    for doc in res['hits']['hits']:
        item_city = {}
        print(doc)
        city_removed = False
        if "Comune soppresso per scorporo" in doc["_source"]:
            city_removed = True

        if city_removed:
            item_city = {
                "City_Name" : doc["_source"]['Denominazione Comune'],
                "City_Code": doc["_source"]['Codice Comune'],
                "Province_Code": doc["_source"]['Sigla Automobilistica'],
                "Suppressed": city_removed
            }
        else:
            item_city = {
                "City_Name" : doc["_source"]['Denominazione (Italiana e straniera)'],
                "City_Code": doc["_source"]['Codice Comune formato alfanumerico'],
                "Province_Code": doc["_source"]['Sigla automobilistica'],
                "Suppressed": city_removed
            }
        response.append(item_city)

    return response