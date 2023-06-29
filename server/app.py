#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    this_animal = Animal.query.filter(Animal.id == id).first()
    response_body = f''
    response_body += f'<ul>ID: {id}</ul>'
    response_body += f'<ul>Name: {this_animal.name}</ul>'
    response_body += f'<ul>Species: {this_animal.species}</ul>'
    response_body += f'<ul>Zookeeper: {this_animal.zookeeper}</ul>'
    response_body += f'<ul>Enclosure: {this_animal.enclosure}</ul>'
    return response_body

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    this_zookeeper = Zookeeper.query.filter(Zookeeper.id == id).first()
    response_body = f''
    response_body += f'<ul>ID: {id}</ul>'
    response_body += f'<ul>Name: {this_zookeeper.name}</ul>'
    response_body += f'<ul>Birthday: {this_zookeeper.birthday}</ul>'
    for animal in this_zookeeper.animals:
        response_body += f'<ul>Animal: {animal.name}</ul>'
    return response_body

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    this_enclosure = Enclosure.query.filter(Enclosure.id == id).first()
    response_body = f''
    response_body += f'<ul>ID: {id}</ul>'
    response_body += f'<ul>Environment: {this_enclosure.environment}</ul>'
    response_body += f'<ul>Open to Visitors: {this_enclosure.open_to_visitors}</ul>'
    return response_body


if __name__ == '__main__':
    app.run(port=5555, debug=True)
