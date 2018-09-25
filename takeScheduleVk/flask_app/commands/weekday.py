from flask_app import command_system
import json

def weekday(body):
    days = ["mon", "tue", "wed", "thu", "fri"]
    ru_days = ["понедельник", "вторник", "среда", "четверг", "пятница"]

    with open("/home/takeSchedule/mysite/flask_app/document.json", encoding="utf-8") as file:
        data_file = json.load(file)
        schedule_global = data_file["schedule"]

    if body == ru_days[0]:
        weekday_now = 0
    elif body == ru_days[1]:
        weekday_now = 1
    elif body == ru_days[2]:
        weekday_now = 2
    elif body == ru_days[3]:
        weekday_now = 3
    elif body == ru_days[4]:
        weekday_now = 4

    schedule_now = schedule_global["odd"][days[weekday_now]]
    subjects = []
    for key in schedule_now["subjects"]:
        time = schedule_now["subjects"][key]["time"]
        subj = schedule_now["subjects"][key]["subj"]
        aud = schedule_now["subjects"][key]["aud"]
        subjects.append("{} {} ({})".format(time, subj, aud))

    message = "{}\nЗдание: {}\nПары:\n{}".format("Числитель",
                                                 schedule_now["building"],
                                                 "\n".join(subjects))

    schedule_now = schedule_global["even"][days[weekday_now]]
    subjects = []
    for key in schedule_now["subjects"]:
        time = schedule_now["subjects"][key]["time"]
        subj = schedule_now["subjects"][key]["subj"]
        aud = schedule_now["subjects"][key]["aud"]
        subjects.append("{} {} ({})".format(time, subj, aud))

    message += "\n\n{}\nЗдание: {}\nПары:\n{}".format("Знаменатель",
                                                 schedule_now["building"],
                                                 "\n".join(subjects))

    return message, ""


weekday_command = command_system.Command()

weekday_command.keys = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница']
weekday_command.description = 'Расписание на определенный день'
weekday_command.process = weekday
