import interactions
from interactions import OptionType, SlashCommand, SlashContext, slash_option, slash_command
from config import BOT_TOKEN, SERVER_ID, CHANNEL_ID
from task import TaskList, Task

client = interactions.Client(
    token=BOT_TOKEN,
    activity=interactions.Activity(
        name="over your to-dos",
        type=interactions.ActivityType.WATCHING
    ),
    debug_scope=SERVER_ID
)

master = TaskList()

@interactions.listen()
async def on_startup():
    """Called when the bot starts."""
    print(f"Logged in as {client.user}.")
    channel = client.get_channel(CHANNEL_ID)
    await channel.send("Todooey is raring to go!")

@slash_command(
    name="show",
    description="Display to-do list."
)
async def show_master(ctx: SlashContext):

    if len(master.tasks) == 0:
        await ctx.send("Nothing to see here. Maybe add a task or two!")
        return
    
    msg_master = []
    for i in range(len(master.tasks)):
        t = master.tasks[i]
        c = "☑️" if t.complete else "⬜"
        msg_master.append(f"{i+1}. {c} {t.description}")
    await ctx.send(("\n").join(msg_master))

base_task = SlashCommand(name="task", description="Base for task commands.")

async def task_id_command(ctx: SlashContext, operation, id: int, *args):
    """
    A reusable function to execute task commands with standardized
    error-handling for the task ID parameter.
    """
    try:
        if id >= 1:
            await operation(id, *args)
        else:
            raise ValueError("Task ID must be strictly positive.")
        
    except ValueError:
        await ctx.send(f"Sorry! I can't do anything with that task ID. Please select a task between 1 and {len(master.tasks)}.")

    except IndexError:
        await ctx.send(f"Task {id} doesn't exist. Sorry!")

@base_task.subcommand(
    sub_cmd_name="add",
    sub_cmd_description="Add a new task to the master list."
)
@slash_option(
    name="description",
    description="Task description.",
    required=True,
    opt_type=OptionType.STRING
)
async def task_add(ctx: SlashContext, description: str):
    master.tasks.append(Task(description))
    await ctx.send(f"\"{description}\" added to the list. Happy tasking!")

@base_task.subcommand(
    sub_cmd_name="check",
    sub_cmd_description="Mark a task is complete/incomplete."
)
@slash_option(
    name="id",
    description="Task number (use /show to check).",
    required=True,
    opt_type=OptionType.INTEGER
)
async def task_check(ctx: SlashContext, id: int):

    async def operation_check(id):
        t = master.tasks[id-1]
        t.complete = not t.complete
        msg_complete = f"\"{t.description}\" complete. Good job!"
        msg_incomplete = f"\"{t.description}\" incomplete. Good luck!"
        await ctx.send(msg_complete if t.complete else msg_incomplete)

    await task_id_command(ctx, operation_check, id)

@base_task.subcommand(
    sub_cmd_name="edit",
    sub_cmd_description="Edit task description."
)
@slash_option(
    name="id",
    description="Task number (use /show to check).",
    required=True,
    opt_type=OptionType.INTEGER
)
@slash_option(
    name="description",
    description="Task description.",
    required=True,
    opt_type=OptionType.STRING    
)
async def task_edit(ctx: SlashContext, id: int, description: str):
    
    async def operation_edit(id, description):
        t = master.tasks[id-1]
        old_desc = t.description
        t.description = description
        msg = f"Task {id} \"{old_desc}\" is now \"{description}\"."
        await ctx.send(msg)

    await task_id_command(ctx, operation_edit, id, description)

@base_task.subcommand(
    sub_cmd_name="delete",
    sub_cmd_description="Delete a task from the master list."
)
@slash_option(
    name="id",
    description="Task number (use /show to check).",
    required=True,
    opt_type=OptionType.INTEGER
)
async def task_delete(ctx: SlashContext, id: int):

    async def operation_delete(id):
        t = master.tasks.pop(id-1)
        msg = f"Task {id} \"{t.description}\" has been deleted."
        await ctx.send(msg)

    await task_id_command(ctx, operation_delete, id)

client.start()
