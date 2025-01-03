from interactions import SlashCommandOption, OptionType
from utils.strings import *

OptionTodoID = SlashCommandOption(
    name=OPT_NAME_TODO_ID,
    description=OPT_DESC_TODO_ID,
    required=True,
    type=OptionType.INTEGER
)

OptionStepID = SlashCommandOption(
    name=OPT_NAME_STEP_ID,
    description=OPT_DESC_STEP_ID,
    required=True,
    type=OptionType.INTEGER
)

OptionDesc = SlashCommandOption(
    name=OPT_NAME_DESC,
    description=OPT_DESC_DESC,
    required=True,
    type=OptionType.STRING
)

OptionTodoIDOptional = SlashCommandOption(
    name=OPT_NAME_TODO_ID,
    description=OPT_DESC_TODO_ID,
    required=False,
    type=OptionType.INTEGER
)