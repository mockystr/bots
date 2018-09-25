# -*- coding: utf-8 -*-
import os
import importlib
from flask_app import vkapi
from flask_app.command_system import command_list
from flask_app import db
from flask_app.models import Subs


# from flask_app import settings
# import datetime
# import json

def get_answer(body, user_id, token):
    message = "Я вас не понимаю. Воспользуйтесь командой \"помощь\""
    attachment = ''

    for c in command_list:
        if body in c.keys:
            if c.keys[0] == "подписка":
                response = vkapi.get_username(user_id, token)[0]
                new_sub = Subs(id=user_id, username=str(response["first_name"] + " " + response["last_name"]))
                try:
                    db.session.add(new_sub)
                    db.session.commit()
                except Exception:
                    return "Ваш id уже в списке рассылки!", ""
            if c.keys[0] == "понедельник":
                message, attachment = c.process(body)
            else:
                message, attachment = c.process()
    return message, attachment


def create_answer(data, token):
    load_modules()
    user_id = data['from_id']
    message, attachment = get_answer(data['text'].lower(), user_id, token)
    vkapi.send_message(user_id, token, message, attachment)


def load_modules():
    # путь от рабочей директории, ее можно изменить в настройках приложения
    files = os.listdir("mysite/flask_app/commands")
    modules = filter(lambda x: x.endswith('.py'), files)
    for m in modules:
        importlib.import_module("flask_app.commands." + m[0:-3])
