# dailyreportbot.py
import discord
from discord import app_commands
from discord.ext import commands
import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
from transformers import T5ForConditionalGeneration, T5Tokenizer

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

try:
    # Load the tokenizer and model
    tokenizer = T5Tokenizer.from_pretrained("vennify/t5-base-grammar-correction")
    model = T5ForConditionalGeneration.from_pretrained("vennify/t5-base-grammar-correction")
except Exception as e:
    print(f"Error loading T5 model: {e}")

# Initialize the bot with intents
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent
bot = commands.Bot(command_prefix="!", intents=intents)

ROLE_TO_DEPARTMENT = {
    "Developer": "Development",
    "QA": "QA",
    "Scrum Master": "Scrum Master",
    # Add more roles and departments as needed
}

def correct_grammar(text):
    # Encode the input text
    input_text = "grammar: " + text  # Prefix as expected by the model
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # Generate the corrected output
    outputs = model.generate(input_ids, max_length=512, do_sample=True, top_k=120, top_p=0.95)
    corrected_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return corrected_text

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

# Slash command: About
@bot.tree.command(name="about", description="About this bot")
async def about(interaction: discord.Interaction):
    about_text = """
    This bot uses the T5 (Text-to-Text Transfer Transformer) model for grammar correction.
    T5 is licensed under the Apache 2.0 License.
    - T5 Model: https://github.com/google-research/text-to-text-transfer-transformer
    - Apache 2.0 License: https://www.apache.org/licenses/LICENSE-2.0.txt
    """
    await interaction.response.send_message(about_text)

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
        username = user.display_name
        department = get_department(user)
        date = datetime.now().strftime("%d %b %Y")
        
        # Fetch tasks from Firestore
        tasks = db.collection('tasks').where('user_nickname', '==', username).stream()
        tasks = [task.to_dict() for task in tasks]
        
        # Organize tasks by type
        organized_tasks = {
            "accomplished": [],
            "blocker": [],
            "ongoing": [],
            "priority": []
        }
        
        for task in tasks:
            if task['task_type'] in organized_tasks:
                organized_tasks[task['task_type']].append(task['task_description'])
        
        # Generate the report
        report = f"""
**Daily Work Report**
-----------------------------
**Prepared by:** {username}
**Department:** {department}
**Date:** {date}

**Accomplished Tasks:**
"""
        if organized_tasks["accomplished"]:
            for task in organized_tasks["accomplished"]:
                report += f"- {task}\n"
        else:
            report += "- No tasks marked as accomplished.\n"
        
        report += """
**Blockers:**
"""
        if organized_tasks["blocker"]:
            for task in organized_tasks["blocker"]:
                report += f"- {task}\n"
        else:
            report += "- No blockers reported.\n"
        
        report += """
**Ongoing Tasks:**
"""
        if organized_tasks["ongoing"]:
            for task in organized_tasks["ongoing"]:
                report += f"- {task}\n"
        else:
            report += "- No ongoing tasks.\n"
        
        report += """
**Priority Tasks:**
"""
        if organized_tasks["priority"]:
            for task in organized_tasks["priority"]:
                report += f"- {task}\n"
        else:
            report += "- No priority tasks.\n"
        
        report += f"""
-----------------------------
**Immediate Supervisor:** Sarah Wilson
**Date Checked:** {date}
"""
        
        # Correct grammar using T5
        corrected_report = correct_grammar(report)
        
        # Send the corrected report to the channel
        await interaction.response.send_message(corrected_report)
    except Exception as e:
        print(f"Error in generate_report: {e}")
        await interaction.response.send_message("An error occurred while generating the report.", ephemeral=True)
        
# Function to get the user's department based on their role
def get_department(member):
    for role in member.roles:
        if role.name in ROLE_TO_DEPARTMENT:
            return ROLE_TO_DEPARTMENT[role.name]
    return "Unknown Department"

# Run the bot
bot.run(os.getenv('DISCORD_BOT_TOKEN'))