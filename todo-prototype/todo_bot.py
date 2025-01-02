import interactions
from interactions import slash_command, slash_option, SlashContext, OptionType, SlashCommand
from config import BOT_TOKEN, SERVER_ID, CHANNEL_ID
from task import TaskList, Todo, Step
from strings import *

#region setup

client = interactions.Client(
    token=BOT_TOKEN,
    activity=interactions.Activity(
        name=ACTIVITY_NAME,
        type=interactions.ActivityType.WATCHING
    ),
    debug_scope=SERVER_ID
)

master = TaskList()

@interactions.listen()
async def on_startup():
    """ Called when the bot starts. """
    print(f"Logged in as {client.user}.")
    channel = client.get_channel(CHANNEL_ID)
    await channel.send("Todooey is raring to go!")

#endregion

#region utility

async def task_id_command(ctx: SlashContext, operation, i: int, *args):
    """
    A reusable function to execute task commands with standardized
    error-handling upon the task ID parameter.
    """
    try:
        if i >= 1:
            await operation(i, *args)
        else:
            raise ValueError(VALUE_ERROR_POSITIVE_TASK_ID)
        
    except ValueError:
        await ctx.send(MSG_VALUE_ERR)

    except IndexError:
        await ctx.send(MSG_INDEX_ERR)

#endregion
)
@slash_option(
    name=OPT_NAME_ID,
    description=OPT_DESC_ID,
    required=True,
    opt_type=OptionType.INTEGER
)
# base_task = SlashCommand(name=CMD_NAME_TASK, description=CMD_DESC_TASK)

# @base_task.subcommand(
#     sub_cmd_name=CMD_NAME_TASK_ADD,
#     sub_cmd_description=CMD_DESC_TASK_ADD
# )
# @slash_option(
#     name=OPT_NAME_DESC,
#     description=OPT_DESC_DESC,
#     required=True,
#     opt_type=OptionType.STRING
# )
# async def task_add(ctx: SlashContext, description: str):
#     master.tasks.append(Task(description))
#     await ctx.send(f"\"{description}\" {MSG_ADD}")

# @base_task.subcommand(
#     sub_cmd_name=CMD_NAME_TASK_CHECK,
#     sub_cmd_description=CMD_DESC_TASK_CHECK
# )
# @slash_option(
#     name=OPT_NAME_ID,
#     description=OPT_DESC_ID,
#     required=True,
#     opt_type=OptionType.INTEGER
# )
# async def task_check(ctx: SlashContext, id: int):

#     async def operation_check(id):
#         t = master.tasks[id-1]
#         t.complete = not t.complete
#         msg_complete = f"\"{t.description}\" {MSG_CHECK_ON}"
#         msg_incomplete = f"\"{t.description}\" {MSG_CHECK_OFF}"
#         await ctx.send(msg_complete if t.complete else msg_incomplete)

#     await task_id_command(ctx, operation_check, id)

# @base_task.subcommand(
#     sub_cmd_name=CMD_NAME_TASK_EDIT,
#     sub_cmd_description=CMD_DESC_TASK_EDIT
# )
# @slash_option(
#     name=OPT_NAME_ID,
#     description=OPT_DESC_ID,
#     required=True,
#     opt_type=OptionType.INTEGER
# )
# @slash_option(
#     name=OPT_NAME_DESC,
#     description=OPT_DESC_DESC,
#     required=True,
#     opt_type=OptionType.STRING    
# )
# async def task_edit(ctx: SlashContext, id: int, description: str):
    
#     async def operation_edit(id, description):
#         t = master.tasks[id-1]
#         old_desc = t.description
#         t.description = description
#         msg = f"Task {id} \"{old_desc}\" {MSG_EDIT} \"{description}\"."
#         await ctx.send(msg)

#     await task_id_command(ctx, operation_edit, id, description)

# @base_task.subcommand(
#     sub_cmd_name=CMD_NAME_TASK_DELETE,
#     sub_cmd_description=CMD_DESC_TASK_DELETE
# )
# @slash_option(
#     name=OPT_NAME_ID,
#     description=OPT_DESC_ID,
#     required=True,
#     opt_type=OptionType.INTEGER
# )
# async def task_delete(ctx: SlashContext, id: int):

#     async def operation_delete(id):
#         t = master.tasks.pop(id-1)
#         msg = f"Task {id} \"{t.description}\" {MSG_DELETE}"
#         await ctx.send(msg)

#     await task_id_command(ctx, operation_delete, id)

client.start()