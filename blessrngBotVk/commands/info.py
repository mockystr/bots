import command_system


def info():
    message = ''
    for c in command_system.command_list:
        message += '&#129305;[' + ', '.join(c.keys) + '] \n&#128526;' + c.description + '\n'
    return message, ''


info_command = command_system.Command()

info_command.keys = ['помощь', 'помоги', 'help']
info_command.description = 'Покажу список команд'
info_command.process = info
