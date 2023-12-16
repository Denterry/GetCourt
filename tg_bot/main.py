import logging
import handlers
import asyncio

from aiogram import Bot, Dispatcher
from database import BotDB
from config import config
from aiogram.types import BotCommand

# from config_data.config import load_config
# config = load_config('tg_bot/dev.env')

BotDB = BotDB('getcourt.db')
bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
dp: Dispatcher = Dispatcher()
logger = logging.getLogger(__name__)

# # Initialize logging
# logging.basicConfig(
#         level=logging.INFO,
#         format='%(filename)s:%(lineno)d #%(levelname)-8s '
#                '[%(asctime)s] - %(name)s - %(message)s')
#
# # Выводим в консоль информацию о начале запуска бота
# logger.info('Starting bot')

# Создаем асинхронную функцию
async def set_main_menu(bot: Bot):
    """
    Создаем список с командами и их описанием для кнопки menu
    :param bot: Bot
    :return: NULL
    """
    main_menu_commands = [
        BotCommand(command='/start',
                   description='Запуск бота'),
        BotCommand(command='/help',
                   description='Справка по работе бота'),
        BotCommand(command='/cancel',
                   description='Отмена действий'),
        BotCommand(command='/support',
                   description='Поддержка'),
        BotCommand(command='/contacts',
                   description='Другие способы связи'),

        BotCommand(command='/add_court',
                   description='Добавление площадки'),
        BotCommand(command='/search_courts',
                   description='Поиск ближайших площадок'),
        BotCommand(command='/start_game',
                   description='Начать активность на площадке'),
        BotCommand(command='/exit_game',
                   description='Закончить активность на площадке'),
        BotCommand(command='/set_event',
                   description='Назначить спортивное мероприятие'),
        BotCommand(command='/payments',
                   description='Платежи')]
    await bot.set_my_commands(main_menu_commands)

async def main():
    """
    Функция конфигурирования и запуска бота
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot')

    dp.include_router(handlers.all_handlers.router)
    dp.startup.register(set_main_menu)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())