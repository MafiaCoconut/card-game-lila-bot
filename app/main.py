import asyncio

from utils import commands, registration_dispatcher
from utils.bot import bot
from utils.logs import logs_settings


async def main() -> None:
    registration_dispatcher.include_routers()

    await commands.set_commands(bot)
    await registration_dispatcher.dp.start_polling(bot)


if __name__ == "__main__":
    logs_settings()
    asyncio.run(main())
