# -*- coding: utf-8 -*-
from flask_app import db

class Subs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60))

    def __repr__(self):
        return "{}-{}".format(self.username, self.id)