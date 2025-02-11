#!/usr/bin/env python3

import string
import random

from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship, validates
from sqlalchemy.ext.hybrid import hybrid_property

from config import db, bcrypt

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    # Database Schema
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    _password_hash = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    age = db.Column(db.Integer)
    room_id = db.Column(db.String, db.ForeignKey('rooms.id'), default=None,)

    # Relationships
    room = db.relationship("Room", back_populates="users")

    # Serialize Rules
    serialize_rules = ("-room.users",)

    # Validations
    @hybrid_property
    def password_hash(self):
        raise AttributeError('Password hashes may not be viewed.')
    
    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')


    # Other Methods
    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))
    
class Room(db.Model, SerializerMixin):
    __tablename__ = 'rooms'

    # Database Schema
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    code = db.Column(db.String(5), unique=True)

    # Relationships
    users = db.relationship("User", back_populates="room")

    # Serialize Rules
    serialize_rules = ("-users.room",)

    # Validations


    # Other Methods


