from typing import Union
from interactions import SlashContext
from .strings import *
from .task import Task, TaskList, Todo

id_index    = lambda i: i-1     # Derive list index from displayed ID.
id_display  = lambda i: i+1     # Derive displayed ID from list index.

async def get_task_safe(task_list: TaskList, i: int, ctx: SlashContext) -> Task:
    """
    A reusable function with standardized error-handling when fetching Task
    objects from a given TaskList instance.
    """
    try:
        if i >= 1:
            return task_list.get_task(id_index(i))
        else:
            raise ValueError(ERROR_POSITIVE_TASK_ID)
    
    except ValueError:
        await ctx.send(MSG_VALUE_ERR(len(task_list)))

    except IndexError:
        await ctx.send(MSG_INDEX_ERR(i))

    return None
    
async def operation_add(target: TaskList, task: Task, ctx: SlashContext, parent_desc: str = ""):
    target.add(task)
    if isinstance(task, Todo):
        await ctx.send(MSG_ADD_TODO(task.description))
    else:
        await ctx.send(MSG_ADD_STEP(task.description, parent_desc))

async def operation_check(target: Task, ctx: SlashContext, parent_desc: str = ""):
    complete = target.check()
    if isinstance(target, Todo):
        await ctx.send(MSG_CHECK_TODO(complete, target.description))
    else:
        await ctx.send(MSG_CHECK_STEP(complete, target.description, parent_desc))

async def operation_edit(target: Task, description: str, ctx: SlashContext, parent_desc: str = ""):
    old_desc = target.edit(description)
    if isinstance(target, Todo):
        await ctx.send(MSG_EDIT_TODO(old_desc, description))
    else:
        await ctx.send(MSG_EDIT_STEP(old_desc, description, parent_desc))

async def operation_delete(target: TaskList, task_id: int, ctx: SlashContext, parent_desc: str = ""):
    task = target.delete(id_index(task_id))
    if isinstance(task, Todo):
        await ctx.send(MSG_DELETE_TODO(task.description))
    else:
        await ctx.send(MSG_DELETE_STEP(task.description, parent_desc))