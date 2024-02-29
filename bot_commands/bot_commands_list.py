from aiogram.types import BotCommand

private = [
    BotCommand(command="movie", description="Случайный Фильм"),
    BotCommand(command="genre_movie", description="Случайный Фильм По Жанру"),
    BotCommand(command="genres", description="Жанры")

]

# If commands change:
# await bot.delete_my_commands(scope=BotCommandScopeDefault())
# await bot.set_my_commands(commands=private, scope=BotCommandScopeDefault())
# for reset commands
