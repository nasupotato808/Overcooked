import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

cred = credentials.Certificate(os.getenv('FIREBASE_KEY_PATH'))
firebase_admin.initialize_app(cred)
db = firestore.client()

task = {
    "user_id": "123",
    "task_type": "accomplished",
    "task_description": "Test task",
    "timestamp": datetime.now().isoformat()
}
db.collection('tasks').add(task)
print("Task added successfully")