#region General
ACTIVITY_NAME = "over the task goblins"
ERROR_POSITIVE_TASK_ID = "Task ID must be strictly positive."
#endregion

# region Names and descriptions of bot commands
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

CMD_NAME_EDIT = "edit"
CMD_DESC_EDIT = "Edit description of a todo or step item."
CMD_DESC_EDIT_TODO = "Edit description of a todo item."
CMD_DESC_EDIT_STEP = "Edit description of a step item under a particular todo item."

CMD_NAME_DELETE = "delete"
CMD_DESC_DELETE = "Delete a todo or stem item."
CMD_DESC_DELETE_TODO = "Delete a todo item from the master list."
CMD_DESC_DELETE_STEP = "Delete a step item from under a particular todo item."
#endregion

# region Names and descriptions of bot command options
OPT_NAME_TODO_ID = "todo_id"
OPT_DESC_TODO_ID = "To-do item number. You can verify this with \"\\show\"."

OPT_NAME_STEP_ID = "step_id"
OPT_DESC_STEP_ID = "Step item number under a specific todo item. You can verify this with \"\\show\"."

OPT_NAME_DESC = "description"
OPT_DESC_DESC = "Task description."
#endregion

# region Bot messages
MSG_SHOW_EMPTY = "Nothing to see here. Maybe add a task or two!"

MSG_ADD_TODO = lambda desc: f"\"{desc}\" added to the list. Happy tasking!"
MSG_ADD_STEP = lambda desc, todo_desc: f"\"{desc}\" added to \"{todo_desc}\". Happy tasking!"

MSG_CHECK_ON = "complete. Good job!"
MSG_CHECK_OFF = "incomplete. Good luck!"
MSG_CHECK_TODO = lambda complete, desc: f"\"{desc}\" {MSG_CHECK_ON if complete else MSG_CHECK_OFF}"
MSG_CHECK_STEP = lambda complete, step_desc, todo_desc: f"\"{step_desc}\" under \"{todo_desc}\" {MSG_CHECK_ON if complete else MSG_CHECK_OFF}"

MSG_EDIT_TODO = lambda old_desc, new_desc: f"\"{old_desc}\" is now \"{new_desc}\"."
MSG_EDIT_STEP = lambda old_desc, new_desc, todo_desc: f"\"{old_desc}\" under \"{todo_desc}\" is now \"{new_desc}\"."

MSG_DELETE_TODO = lambda desc: f"\"{desc}\" has been deleted from the master list."
MSG_DELETE_STEP = lambda step_desc, todo_desc: f"\"{step_desc}\" has been deleted from under \"{todo_desc}\"."

MSG_VALUE_ERR = lambda n: f"Sorry! I can't do anything with that task ID. Please select a task between 1 and {n}."
MSG_INDEX_ERR = lambda i: f"Task {i} doesn't exist. Sorry!"
#endregion

# region Object strings
INDENT = "      "
NUMBERING = lambda i: f"{f'#{(i)}':>4}"
WHITESPACE = "\u200b"
CHECKBOX = lambda complete: "✅" if complete else "⬜"
# endregion

#region Modal fields
FIELD_LABEL_TODO_ID = "Todo ID"
FIELD_ID_TODO_ID = "todo_id"

FIELD_LABEL_STEP_ID = "Step ID"
FIELD_ID_STEP_ID = "step_id"

FIELD_LABEL_DESCRIPTION = "Task Description"
FIELD_ID_DESCRIPTION = "task_description"

FIELD_LABEL_DELETE = "Are you sure you want to delete this item?"
FIELD_ID_DELETE = "confirm_delete"

FIELD_PLACEHOLDER_INT = "e.g. 1"
FIELD_PLACEHOLDER_STR = "e.g. do laundry"
FIELD_PLACEHOLDER_YES = "Type 'YES' to confirm deletion."
#endregion

#region Modals and buttons
TXT_ADD_TODO = "➕ Add Todo"
MOD_ADD_TODO = "mod_add_todo"
BTN_ADD_TODO = "btn_add_todo"

TXT_ADD_STEP = "➕ Add Step"
MOD_ADD_STEP = "mod_add_step"
BTN_ADD_STEP = "btn_add_step"

TXT_CHECK_TODO = "✅ Check Todo"
BTN_CHECK_TODO = "btn_check_todo"

TXT_CHECK_STEP = "✅ Check Step"
MOD_CHECK_STEP = "mod_check_step"
BTN_CHECK_STEP = "btn_check_step"

TXT_EDIT_TODO = "✏️ Edit Todo"
MOD_EDIT_TODO = "mod_edit_todo"
BTN_EDIT_TODO = "btn_edit_todo"

TXT_EDIT_STEP = "✏️ Edit Step"
MOD_EDIT_STEP = "mod_edit_step"
BTN_EDIT_STEP = "btn_edit_step"

TXT_DELETE_TODO = "❌ Delete Todo"
MOD_DELETE_TODO = "mod_delete_todo"
BTN_DELETE_TODO = "btn_delete_todo"

TXT_DELETE_STEP = "❌ Delete Step"
MOD_DELETE_STEP = "mod_delete_step"
BTN_DELETE_STEP = "btn_delete_step"

TXT_VIEW_TODO = "🔍 View Todo"
MOD_VIEW_TODO = "mod_view_todo"
BTN_VIEW_TODO = "btn_view_todo"

TXT_BACK = "⬅️ Back"
BTN_BACK = "btn_back_todo"

TXT_BREAK_TODO = "🪄 Coming soon..."
MOD_BREAK_TODO = "mod_break_todo"
BTN_BREAK_TODO = "btn_break_todo"
#endregion

# region Embeds
EMBED_COLOR = 0x5fdcb6
EMBED_TITLE_MASTER = lambda guild_name: f"{guild_name}'s To-do List"
EMBED_DESC_MASTER = "There's much to be done!"
EMBED_DESC_TODO = lambda complete: f"`Completion status: {CHECKBOX(complete)}`"
#endregion