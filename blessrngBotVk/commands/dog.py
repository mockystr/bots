import command_system
import vkapi
import settings


def dog():
    # Получаем случайную картинку из паблика
    attachment = vkapi.get_random_wall_picture(-134182185, settings.access_token)
    message = 'roflanSobaka.'
    return message, attachment


dog_command = command_system.Command()

dog_command.keys = ['пес', 'собака', 'собакен', 'sobaka', 'dog', 'doge', 'doggo', 'песель', 'песа', 'песы', 'собачка',
                    'стас']
dog_command.description = 'Кину тебе песу'
dog_command.process = dog
