from typing import Union
from interactions import Embed, SlashContext
from config import master
from utils.strings import *
from utils.task import Task, TaskList, Todo
from utils.operations import id_index, id_display

def create_embed(task_list: TaskList, title: str, desc: str) -> Embed:
    embed = Embed(title=title, description=desc, color=EMBED_COLOR)

    for i in range(len(task_list)):
        task = task_list.get_task(i)
        render_string = f"{NUMBERING(i+1)} {task}"
        embed.add_field(name=WHITESPACE, value=f"```{render_string}```", inline=False)

    return embed

async def operation_show(target: Union[TaskList, Todo], ctx: SlashContext):
    if isinstance(target, TaskList):
        guild_name = ctx.guild.name if ctx.guild else "Unknown Server"
        embed = create_embed(target, EMBED_TITLE_MASTER(guild_name), EMBED_DESC_MASTER)
    else:
        embed = create_embed(target.steps, target.description, EMBED_DESC_TODO(target.complete))
    await ctx.send(embeds=[embed])