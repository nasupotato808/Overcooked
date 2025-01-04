import discord
from discord import app_commands
from discord.ext import commands
import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Initialize Firebase
try:
    cred = credentials.Certificate(os.getenv('FIREBASE_KEY_PATH'))
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    print("Firebase initialized successfully")
except Exception as e:
    print(f"Error initializing Firebase: {e}")

# Initialize the bot with intents
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: When the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    try:
        # Sync slash commands
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

# Slash command: Ping
@bot.tree.command(name="ping", description="Check if the bot is alive")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")

# Slash command: Add Task
@bot.tree.command(name="addtask", description="Add a task to your to-do list")
@app_commands.describe(
    task_type="Type of task (accomplished, blocker, ongoing, priority)",
    task_description="Description of the task"
)
async def add_task(interaction: discord.Interaction, task_type: str, task_description: str):
    try:
        user_id = interaction.user.id
        task = {
            "user_id": user_id,
            "task_type": task_type,
            "task_description": task_description,
            "timestamp": datetime.now().isoformat()  # Correct usage of datetime
        }
        db.collection('tasks').add(task)
        await interaction.response.send_message(f"Task added: {task_description}")
    except Exception as e:
        print(f"Error in add_task: {e}")
        await interaction.response.send_message("An error occurred while adding the task.", ephemeral=True)

# Slash command: Generate Report
@bot.tree.command(name="generatereport", description="Generate a daily report based on your to-do list")
async def generate_report(interaction: discord.Interaction):
    try:
        user = interaction.user
        username = user.name
        department = get_department(user)
        date = datetime.now().strftime("%d %b %Y")
        
        # Fetch tasks from Firestore
        tasks = db.collection('tasks').where('user_id', '==', user.id).stream()
        tasks = [task.to_dict() for task in tasks]
        
        # Generate the report
        report = f"""
Prepared by: {username}
Last Updated: {date}
Department: {department}

Accomplished Tasks:
"""
        for task in tasks:
            if task['task_type'] == 'accomplished':
                report += f"- {task['task_description']}\n"
        
        report += "\nBlockers:\n"
        for task in tasks:
            if task['task_type'] == 'blocker':
                report += f"- {task['task_description']}\n"
        
        report += f"""
Immediate Supervisor: Sarah Wilson
Date Checked: {date}
"""
        
        # Send the report to the channel
        await interaction.response.send_message(report)
    except Exception as e:
        print(f"Error in generate_report: {e}")
        await interaction.response.send_message("An error occurred while generating the report.", ephemeral=True)

# Function to get the user's department based on their role
def get_department(member):
    role_to_department = {
        "Developer": "Development",
        "QA": "QA",
        "Scrum Master": "Scrum Master",
    }
    for role in member.roles:
        if role.name in role_to_department:
            return role_to_department[role.name]
    return "Unknown Department"

# Run the bot
bot.run(os.getenv('DISCORD_BOT_TOKEN'))