import falcon
from falcon import API

from api.resources import HomeResource, PersonResource, PersonSingleResource

# Resources are represented by long-lived class instances
home_resource = HomeResource()
person_single_resource = PersonSingleResource()
person_resource = PersonResource()


# API configuration
def get_api() -> API:
    _api = falcon.API()
    _api.add_route('/', home_resource)
    _api.add_route('/person/', person_resource)
    _api.add_route('/person/{id}', person_single_resource)


    return _api
