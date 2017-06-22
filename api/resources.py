import json
from argparse import Namespace

import falcon

from api.db import db_session
from api.models import Person

session = db_session


class HomeResource(object):
    def on_get(self, req, resp):
        resp.body = 'Hello World!'
        resp.status = falcon.HTTP_200


class PersonSingleResource(object):
    """
     Handles GET request
    """
    def on_get(self, req, resp, id):
        person = session.query(Person).filter_by(id=id).first()
        if person:
            resp.status = falcon.HTTP_200
            resp.body = str(person.__dict__)
        else:
            resp.status = falcon.HTTP_404
            resp.body = str({'message': 'Person with id:' + id + ' not found !!'})


class PersonResource(object):
    """
    Handles GET request to serve all person list
    """
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        persons = session.query(Person).order_by(Person.id).all()
        resp.body = str([prsn.__dict__ for prsn in persons])

    """
    Handles POST request
    """
    def on_post(self, req, resp):
        body = json.loads(req.stream.read(), object_hook=lambda d: Namespace(**d))
        session.add(Person(name=body.name, age=body.age))
        session.commit()
        session.close()
