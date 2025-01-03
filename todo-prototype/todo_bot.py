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

master.add(Todo("do laundry"))
master.add(Todo("do the dishes"))
master.add(Todo("pay bills"))
master.get_task(0).steps.add(Step("sort lights and darks"))
master.get_task(0).steps.add(Step("load laundry into washing machine"))
master.get_task(0).steps.add(Step("hang delicates out to dry"))
master.get_task(0).steps.add(Step("load remaining laundry into dryer"))
master.get_task(0).steps.add(Step("fold clothes and stow in closet"))
#endregion

#region utility
async def get_task(task_list: TaskList, i: int, ctx: SlashContext) -> Task:
    """
    A reusable function with error-handling for task-fetching commands.
    """
    try:
        if i >= 1:
            return task_list.get_task(i-1)
        else:
            raise ValueError(ERROR_POSITIVE_TASK_ID)
    
    except ValueError:
        await ctx.send(MSG_VALUE_ERR(len(task_list)))

    except IndexError:
        await ctx.send(MSG_INDEX_ERR(i))

    return None
#endregion

#region options
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
#endregion
)
async def show(ctx: SlashContext, todo_id: int = 0):

    # To-do item not specified so display entire list.
    if todo_id == 0:
        if master.is_empty():
            await ctx.send(MSG_SHOW_EMPTY)
        else:
            await ctx.send(str(master))

    else:
        await task_id_command(ctx, operation_show, todo_id)

#endregion

#region /todo

base_task = SlashCommand(name=CMD_NAME_TASK, description=CMD_DESC_TASK)

#endregion

#region /step

base_step = SlashCommand()

#endregion

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