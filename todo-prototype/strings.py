ACTIVITY_NAME = "over the task goblins"
ERROR_POSITIVE_TASK_ID = "Task ID must be strictly positive."
INDENT = "    "

# Names and descriptions of bot commands.

CMD_NAME_SHOW = "show"
CMD_DESC_SHOW = "Display all your tasks or the details of a specific task."

CMD_NAME_TASK = "task"
CMD_DESC_TASK = "Create, modify, or delete tasks."

CMD_NAME_TASK_ADD = "add"
CMD_DESC_TASK_ADD = "Create a new task."

CMD_NAME_TASK_CHECK = "check"
CMD_DESC_TASK_CHECK = "Toggle task completion status."

CMD_NAME_TASK_EDIT = "edit"
CMD_DESC_TASK_EDIT = "Edit task description."

CMD_NAME_TASK_DELETE = "delete"
CMD_DESC_TASK_DELETE = "Delete task."

# Names and descriptions of bot command options.

OPT_NAME_TODO_ID = "todo-id"
OPT_DESC_TODO_ID = "To-do item number. You can verify this with \"\\show\"."

OPT_NAME_DESC = "description"
OPT_DESC_DESC = "Task description."

# Bot messages.

MSG_SHOW_EMPTY = "Nothing to see here. Maybe add a task or two!"
MSG_ADD = "added to the list. Happy tasking!"
MSG_CHECK_ON = "complete. Good job!"
MSG_CHECK_OFF = "incomplete. Good luck!"
MSG_EDIT = "is now"
MSG_DELETE = "has been deleted."
MSG_VALUE_ERR = "Sorry! I can't do anything with that task ID. Please select a task between 1 and"
MSG_INDEX_ERR = lambda i: f"Task {i} doesn't exist. Sorry!"