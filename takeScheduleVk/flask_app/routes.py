# -*- coding: utf-8 -*-
from flask_app import app
# from flask_app.models import Subs
from flask_app import settings, messageHandler
from flask import request, json
import datetime
from flask_app.models import Subs
from flask_app import vkapi

@app.route('/')
def hello_world():
    return 'Hello from Flask!'


@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)

    if 'type' not in data.keys():
        return 'not vk'
    elif data['type'] == 'confirmation':
        return settings.confirmation_token
    elif data['type'] == 'message_new':
        messageHandler.create_answer(data['object'], settings.token)
        return 'ok'

@app.route('/setweek', methods=['POST'])
def set_week():
    try:
        if request.method == "POST":
            if request.values.get('user') == "emir228":
                with open("/home/takeSchedule/mysite/flask_app/document.json", 'r+', encoding='utf-8') as f:
                    data = json.load(f)
                    if data["week_type"] == u"even":
                        data["week_type"] = u"odd"
                    else:
                        data["week_type"] = u"even"

                    f.seek(0)
                    json.dump(data, f, indent=2, ensure_ascii=False)
                    f.truncate()
                return "success"
            return "wrong data"
    except:
        return "error"

# @app.route('/subs', methods=['GET','POST'])
# def write_to_subs():
#     try:
#         if request.method == 'POST':
#             if request.values.get('user') == "emir228":
#                 days = ["mon", "tue", "wed", "thu", "fri"]
#                 ru_days = ["понедельник", "вторник", "среда", "четверг", "пятница"]

#                 with open("/home/takeSchedule/mysite/flask_app/document.json", encoding="utf-8") as file:
#                     schedule_global = json.load(file)["schedule"]

#                 weekday_now = datetime.datetime.today().weekday()
#                 weekday_now = 4
#                 schedule_now = schedule_global["odd"][days[weekday_now]]

#                 subjects = []
#                 for key in schedule_now["subjects"]:
#                     time = schedule_now["subjects"][key]["time"]
#                     subj = schedule_now["subjects"][key]["subj"]
#                     aud = schedule_now["subjects"][key]["aud"]
#                     subjects.append("{} {} ({})".format(time, subj, aud))

#                 message = "{}, {}\nЗдание: {}\nПары:\n{}".format(datetime.date.today(), ru_days[weekday_now].capitalize(),
#                                                              schedule_now["building"],
#                                                              "\n".join(subjects))

#                 all_subs = Subs.query.all()

#                 for sub in all_subs:
#                     vkapi.send_message(sub.id, settings.token, message, "")

#                 return "success"
#             return "error occured"
#         else:
#             return "hello, sub"
#     except:
#         return "wrong data"

@app.route('/subs', methods=['GET','POST'])
def write_to_subs():
    try:
        if request.method == 'POST':
            if request.values.get('user') == "emir228":
                days = ["mon", "tue", "wed", "thu", "fri"]
                ru_days = ["понедельник", "вторник", "среда", "четверг", "пятница"]

                with open("/home/takeSchedule/mysite/flask_app/document.json", encoding="utf-8") as file:
                    data_file = json.load(file)
                    schedule_global = data_file["schedule"]
                    week_type = data_file["week_type"]
                weekday_now = datetime.datetime.today().weekday()
                schedule_now = schedule_global[week_type][days[weekday_now]]

                subjects = []
                for key in schedule_now["subjects"]:
                    time = schedule_now["subjects"][key]["time"]
                    subj = schedule_now["subjects"][key]["subj"]
                    aud = schedule_now["subjects"][key]["aud"]
                    subjects.append("{} {} ({})".format(time, subj, aud))

                message = "{}, {}\nЗдание: {}\nПары:\n{}".format(datetime.date.today(), ru_days[weekday_now].capitalize(),
                                                             schedule_now["building"],
                                                             "\n".join(subjects))

                all_subs = Subs.query.all()

                for sub in all_subs:
                    vkapi.send_message(sub.id, settings.token, message, "")

                return "success"
            return "error occured"
        else:
            return "hello, sub"
    except:
        return "wrong data"