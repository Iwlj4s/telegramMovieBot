from aiogram.types import BotCommand

private = [
    BotCommand(command="movie", description="Random Movie"),
    BotCommand(command="genre_movie", description="Random Movie By Genre"),
    BotCommand(command="genres", description="Genres")

]

# If commands change:
# await bot.delete_my_commands(scope=BotCommandScopeDefault())
# await bot.set_my_commands(commands=private, scope=BotCommandScopeDefault())
# for reset commands
