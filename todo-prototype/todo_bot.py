import interactions
from interactions import SlashCommandOption, slash_command, SlashContext, OptionType, SlashCommand
from config import BOT_TOKEN, SERVER_ID, CHANNEL_ID, master
from task import Task, TaskList, Todo, Step
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

#region /show
@slash_command(
    name=CMD_NAME_SHOW,
    description=CMD_DESC_SHOW,
    options=[OptionTodoIDOptional]
)
async def show(ctx: SlashContext, todo_id: int = 0):
    if master.is_empty():
        await ctx.send(MSG_SHOW_EMPTY)
        return
    
    if todo_id == 0:
        await ctx.send(f"```{str(master)}```")

    else:
        todo = await get_task(master, todo_id, ctx)
        if todo is not None:
            await ctx.send(f"```{str(todo)}```")
#endregion

#region /add
base_add = SlashCommand(
    name=CMD_NAME_ADD,
    description=CMD_DESC_ADD
)

@base_add.subcommand(
    sub_cmd_name=CMD_SUB_NAME_TODO,
    sub_cmd_description=CMD_DESC_ADD_TODO,
    options=[OptionDesc]
)
async def add_todo(ctx: SlashContext, description: str):
    master.add(Todo(description))
    await ctx.send(MSG_ADD_TODO(description))

@base_add.subcommand(
    sub_cmd_name=CMD_SUB_NAME_STEP,
    sub_cmd_description=CMD_DESC_ADD_STEP,
    options=[OptionTodoID, OptionDesc]
)
async def add_step(ctx: SlashContext, todo_id: int, description: str):
    todo = await get_task(master, todo_id, ctx)
    if todo is not None:
        todo.steps.add(Step(description))
        await ctx.send(MSG_ADD_STEP(description, todo.description))
#endregion

#region /check
base_check = SlashCommand(
    name=CMD_NAME_CHECK,
    description=CMD_DESC_CHECK
)

@base_check.subcommand(
    sub_cmd_name=CMD_SUB_NAME_TODO,
    sub_cmd_description=CMD_DESC_CHECK_TODO,
    options=[OptionTodoID]
)
async def check_todo(ctx: SlashContext, todo_id: int):
    todo = await get_task(master, todo_id, ctx)
    if todo is not None:
        complete = todo.check()
        await ctx.send(MSG_CHECK_TODO(complete, todo.description))

@base_check.subcommand(
    sub_cmd_name=CMD_SUB_NAME_STEP,
    sub_cmd_description=CMD_DESC_CHECK_STEP,
    options=[OptionTodoID, OptionStepID]
)
async def check_step(ctx: SlashContext, todo_id: int, step_id: int):
    todo = await get_task(master, todo_id, ctx)
    if todo is not None:
        step = await get_task(todo.steps, step_id, ctx)
        if step is not None:
            complete = step.check()
            await ctx.send(MSG_CHECK_STEP(complete, step.description, todo.description))
#endregion

#region /edit
base_edit = SlashCommand(
    name=CMD_NAME_EDIT,
    description=CMD_DESC_EDIT
)

@base_edit.subcommand(
    sub_cmd_name=CMD_SUB_NAME_TODO,
    sub_cmd_description=CMD_DESC_EDIT_TODO,
    options=[OptionTodoID, OptionDesc]
)
async def edit_todo(ctx: SlashContext, todo_id: int, description: str):
    todo = await get_task(master, todo_id, ctx)
    if todo is not None:
        old_desc = todo.edit(description)
        await ctx.send(MSG_EDIT_TODO(old_desc, description))

@base_edit.subcommand(
    sub_cmd_name=CMD_SUB_NAME_STEP,
    sub_cmd_description=CMD_DESC_EDIT_STEP,
    options=[OptionTodoID, OptionStepID, OptionDesc]
)
async def edit_step(ctx: SlashContext, todo_id: int, step_id: int, description: str):
    todo = await get_task(master, todo_id, ctx)
    if todo is not None:
        step = await get_task(todo.steps, step_id, ctx)
        if step is not None:
            old_desc = step.edit(description)
            await ctx.send(MSG_EDIT_STEP(old_desc, description, todo.description))
#endregion

#region /delete
base_delete = SlashCommand(
    name=CMD_NAME_DELETE,
    description=CMD_DESC_DELETE
)

@base_delete.subcommand(
    sub_cmd_name=CMD_SUB_NAME_TODO,
    sub_cmd_description=CMD_DESC_DELETE_TODO,
    options=[OptionTodoID]
)
async def delete_todo(ctx: SlashContext, todo_id: int):
    todo = await get_task(master, todo_id, ctx)
    if todo is not None:
        desc = master.delete(todo_id-1).description
        await ctx.send(MSG_DELETE_TODO(desc))

@base_delete.subcommand(
    sub_cmd_name=CMD_SUB_NAME_STEP,
    sub_cmd_description=CMD_DESC_DELETE_STEP,
    options=[OptionTodoID, OptionStepID]
)
async def delete_step(ctx: SlashContext, todo_id: int, step_id: int):
    todo = await get_task(master, todo_id, ctx)
    if todo is not None:
        step = await get_task(todo.steps, step_id, ctx)
        if step is not None:
            desc = todo.steps.delete(step_id-1).description
            await ctx.send(MSG_DELETE_STEP(desc, todo.description))
#endregion

client.start()