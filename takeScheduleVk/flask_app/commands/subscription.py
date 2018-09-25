from flask_app import command_system

def subs():
    message = 'Вы подписались на ежедневную рассылку расписания!'
    return message, ''


sub_command = command_system.Command()

sub_command.keys = ['подписка', 'подписаться', 'subscription']
sub_command.description = 'Подписка на рассылку расписания с понедельника по пятницу в 7:30'
sub_command.process = subs
