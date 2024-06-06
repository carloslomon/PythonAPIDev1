import sys
 
# setting path
sys.path.append('../../resources')
sys.path.append('../imdb_resources')
 

from resources.mysql_data_service import MySQLDataService, MySQLDataServiceConfig
from resources.imdb_resources.artist_resource import ArtistResource
import json
from service_factory import ServiceFactory

service_factory = ServiceFactory()
artist_resource = service_factory.get_resource("ArtistResource")


def t1():

    a_resource = artist_resource
    result = a_resource.get_by_key("nm0727778")
    print("t1: result = \n", json.dumps(result.dict(), indent=2))


def t2():

    a_resource = artist_resource
    result = a_resource.get(primaryName='Sophie Turner')
    print("t2: result = \n", json.dumps(result.dict(), indent=2))

def t3():
    a_resource = artist_resource
    result = a_resource.post({"nconst": "nm6969690", "primaryName": "Joe Schmoe", "birthYear": "1969"})
    print("t3: result = \n", result)

def t4():

    a_resource = artist_resource
    result = a_resource.get(primaryName='Sophie Turner')
    print("t2: result = \n", json.dumps(result.dict(), indent=2))

def t5():
    a_resource = artist_resource
    result = a_resource.update(primaryName = "Joe Schmoe", newValues = {"deathYear": "1971"})
    print("t3: result = \n", result)




if __name__ == "__main__":
    #t1()
    t2()
    