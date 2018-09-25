import vkapi
import os
import importlib
from command_system import command_list
import random


def get_answer(body):
    message = "Прости, не понимаю тебя. Напиши 'помощь', чтобы узнать мои команды"
    attachment = ''

    if body.startswith("рандом") or body.startswith("random") or body.startswith("blessrng") or body.startswith(
            "rngpls") or body.startswith("rand"):
        try:
            body = body.split(' ')[1]
        except IndexError:
            return message, attachment

        try:
            interval = [int(i) for i in body.split(';')]

            if len(interval) == 2:
                message = random.randrange(min(interval), max(interval))
                return message, attachment
            else:
                return interval[random.randint(0, len(interval))], attachment
        except ValueError:
            interval = body.split(';')
            return interval[random.randint(0, len(interval) - 1)], attachment
    else:
        for c in command_list:
            if body in c.keys:
                message, attachment = c.process()
        return message, attachment


def create_answer(data, token):
    load_modules()
    user_id = data['from_id']
    message, attachment = get_answer(data['text'].lower())
    vkapi.send_message(user_id, token, message, attachment)


def load_modules():
    # путь от рабочей директории, ее можно изменить в настройках приложения
    files = os.listdir("mysite/commands")
    modules = filter(lambda x: x.endswith('.py'), files)
    for m in modules:
        importlib.import_module("commands." + m[0:-3])
