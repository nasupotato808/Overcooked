from interactions import slash_command, SlashCommand, SlashContext
from config import master
from utils.task import Todo, Step
from utils.operations import get_task_safe, operation_add, operation_check, operation_edit, operation_delete
from .options import *
from ui_components.show_embed import operation_show

#region /show
@slash_command(
    name=CMD_NAME_SHOW,
    description=CMD_DESC_SHOW,
    options=[OptionTodoIDOptional]
)
async def show(ctx: SlashContext, todo_id: int = 0):
    if todo_id == 0:
        await operation_show(master, ctx)
    else:
        todo = await get_task_safe(master, todo_id, ctx)
        if todo is not None:
            await operation_show(todo, ctx)
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
    await operation_add(master, Todo(description), ctx)

@base_add.subcommand(
    sub_cmd_name=CMD_SUB_NAME_STEP,
    sub_cmd_description=CMD_DESC_ADD_STEP,
    options=[OptionTodoID, OptionDesc]
)
async def add_step(ctx: SlashContext, todo_id: int, description: str):
    todo = await get_task_safe(master, todo_id, ctx)
    if todo is not None:
        await operation_add(todo.steps, Step(description), ctx, todo.description)
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
    todo = await get_task_safe(master, todo_id, ctx)
    if todo is not None:
        await operation_check(todo, ctx)

@base_check.subcommand(
    sub_cmd_name=CMD_SUB_NAME_STEP,
    sub_cmd_description=CMD_DESC_CHECK_STEP,
    options=[OptionTodoID, OptionStepID]
)
async def check_step(ctx: SlashContext, todo_id: int, step_id: int):
    todo = await get_task_safe(master, todo_id, ctx)
    if todo is not None:
        step = await get_task_safe(todo.steps, step_id, ctx)
        if step is not None:
            await operation_check(step, ctx, todo.description)
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
    todo = await get_task_safe(master, todo_id, ctx)
    if todo is not None:
        await operation_edit(todo, description, ctx)

@base_edit.subcommand(
    sub_cmd_name=CMD_SUB_NAME_STEP,
    sub_cmd_description=CMD_DESC_EDIT_STEP,
    options=[OptionTodoID, OptionStepID, OptionDesc]
)
async def edit_step(ctx: SlashContext, todo_id: int, step_id: int, description: str):
    todo = await get_task_safe(master, todo_id, ctx)
    if todo is not None:
        step = await get_task_safe(todo.steps, step_id, ctx)
        if step is not None:
            await operation_edit(step, description, ctx, todo.description)
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
    todo = await get_task_safe(master, todo_id, ctx)
    if todo is not None:
        await operation_delete(master, todo_id, ctx)

@base_delete.subcommand(
    sub_cmd_name=CMD_SUB_NAME_STEP,
    sub_cmd_description=CMD_DESC_DELETE_STEP,
    options=[OptionTodoID, OptionStepID]
)
async def delete_step(ctx: SlashContext, todo_id: int, step_id: int):
    todo = await get_task_safe(master, todo_id, ctx)
    if todo is not None:
        step = await get_task_safe(todo.steps, step_id, ctx)
        if step is not None:
            await operation_delete(todo.steps, step_id, ctx, todo.description)
#endregion