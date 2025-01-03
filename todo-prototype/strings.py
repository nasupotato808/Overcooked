ACTIVITY_NAME = "over the task goblins"
ERROR_POSITIVE_TASK_ID = "Task ID must be strictly positive."
INDENT = "    "

# Names and descriptions of bot commands.

CMD_SUB_NAME_TODO = "todo"
CMD_SUB_NAME_STEP = "step"

CMD_NAME_SHOW = "show"
CMD_DESC_SHOW = "Display all tasks or the details of a specific todo item."

CMD_NAME_ADD = "add"
CMD_DESC_ADD = "Add a new todo or step item."
CMD_DESC_ADD_TODO = "Add a new todo item to the master list."
CMD_DESC_ADD_STEP = "Add a new step item under an existing todo item."

CMD_NAME_CHECK = "check"
CMD_DESC_CHECK = "Toggle completion status of a todo or step item."
CMD_DESC_CHECK_TODO = "Toggle completion status of a todo item."
CMD_DESC_CHECK_STEP = "Toggle completion status of a step item under a particular todo item."

CMD_NAME_TASK_EDIT = "edit"
CMD_DESC_TASK_EDIT = "Edit task description."

CMD_NAME_TASK_DELETE = "delete"
CMD_DESC_TASK_DELETE = "Delete task."

# Names and descriptions of bot command options.

OPT_NAME_TODO_ID = "todo_id"
OPT_DESC_TODO_ID = "To-do item number. You can verify this with \"\\show\"."

OPT_NAME_STEP_ID = "step_id"
OPT_DESC_STEP_ID = "Step item number under a specific todo item. You can verify this with \"\\show\"."

OPT_NAME_DESC = "description"
OPT_DESC_DESC = "Task description."

# Bot messages.

MSG_SHOW_EMPTY = "Nothing to see here. Maybe add a task or two!"

MSG_ADD_TODO = lambda desc: f"\"{desc}\" added to the list. Happy tasking!"
MSG_ADD_STEP = lambda desc, todo_desc: f"\"{desc}\"added to \"{todo_desc}\". Happy tasking!"

MSG_CHECK_ON = "complete. Good job!"
MSG_CHECK_OFF = "incomplete. Good luck!"
MSG_EDIT = "is now"
MSG_DELETE = "has been deleted."
MSG_VALUE_ERR = lambda n: f"Sorry! I can't do anything with that task ID. Please select a task between 1 and {n}."
MSG_INDEX_ERR = lambda i: f"Task {i} doesn't exist. Sorry!"