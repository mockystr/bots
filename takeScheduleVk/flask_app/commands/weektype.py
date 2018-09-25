from flask_app import command_system
import json

def weektype():
    with open("/home/takeSchedule/mysite/flask_app/document.json", encoding="utf-8") as file:
        data_file = json.load(file)
        week_type = data_file["week_type"]

    if week_type == 'odd':
        message = 'Числитель'
    else:
        message = 'Знаменатель'
    return message, ""


weektype_command = command_system.Command()

weektype_command.keys = ['неделя', 'тип недели']
weektype_command.description = 'Сегодня числитель или знаменатель?'
weektype_command.process = weektype
