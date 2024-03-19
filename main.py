import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers

# Инициалзация логгера
logger = logging.getLogger(__name__)

#Функция запуска бота
async def main():
    # Конфигурируем логгирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
                '[%(asctime)s] - %(name)s - %(message)s')
    #Вывод,что бот запущен
    logger.info('Starting bot')

    #Загрузка конфига в переменную config
    config: Config = load_config()

    # Инициализация бота и диспетчера
    bot = Bot(token=config.tg_bot.token)#,
              #parse_mode='HTML')
    dp = Dispatcher()

    # Регистрация роутеров
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # Пропускаем накопившиеся апдейты и запускаем поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())