import interactions
from config import BOT_TOKEN, SERVER_ID, CHANNEL_ID, master
from utils.task import Todo, Step
from utils.strings import *
from commands.commands import *

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

client.start()