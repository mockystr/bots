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
                new_sub = Subs(id=user_id, username = str(response["first_name"] + " " + response["last_name"]))
                try:
                    db.session.add(new_sub)
                    db.session.commit()
                except Exception:
                    return "Ваш id уже в списке рассылки!", ""
            message, attachment = c.process()
    return message, attachment


def create_answer(data, token):
    load_modules()
    user_id = data['from_id']
    message, attachment = get_answer(data['text'].lower(), user_id, token)
    vkapi.send_message(user_id, token, message, attachment)

# def write_to_subs():
#     days = ["mon", "tue", "wed", "thu", "fri"]
#     ru_days = ["понедельник", "вторник", "среда", "четверг", "пятница"]

#     with open("flask_app/document.json", encoding="utf-8") as file:
#         schedule_global = json.load(file)["schedule"]

#     weekday_now = datetime.datetime.today().weekday()
#     schedule_now = schedule_global["odd"][days[weekday_now]]

#     subjects = []
#     for key in schedule_now["subjects"]:
#         time = schedule_now["subjects"][key]["time"]
#         subj = schedule_now["subjects"][key]["subj"]
#         aud = schedule_now["subjects"][key]["aud"]
#         subjects.append("{} {} ({})".format(time, subj, aud))

#     message = "{}, {}\nЗдание: {}\nПары:\n{}".format(datetime.date.today(), ru_days[weekday_now].capitalize(),
#                                                  schedule_now["building"],
#                                                  "\n".join(subjects))

#     all_subs = Subs.query.all()

#     for sub in all_subs:
#         vkapi.send_message(sub.id, settings.token, message, "")


def load_modules():
    # путь от рабочей директории, ее можно изменить в настройках приложения
    files = os.listdir("mysite/flask_app/commands")
    modules = filter(lambda x: x.endswith('.py'), files)
    for m in modules:
        importlib.import_module("flask_app.commands." + m[0:-3])
