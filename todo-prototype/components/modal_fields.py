from interactions import ShortText
from utils.strings import *

field_todo_id = ShortText(
    label=FIELD_LABEL_TODO_ID,
    custom_id=FIELD_ID_TODO_ID,
    required=True,
    placeholder=FIELD_PLACEHOLDER_INT,
    min_length=1
)

field_step_id = ShortText(
    label=FIELD_LABEL_STEP_ID,
    custom_id=FIELD_ID_STEP_ID,
    required=True,
    placeholder=FIELD_PLACEHOLDER_INT,
    min_length=1
)

field_description = ShortText(
    label=FIELD_LABEL_DESCRIPTION,
    custom_id=FIELD_ID_DESCRIPTION,
    required=True,
    placeholder=FIELD_PLACEHOLDER_STR,
    min_length=1
)

field_confirm_delete = ShortText(
    label=FIELD_LABEL_DELETE,
    custom_id=FIELD_ID_DELETE,
    required=True,
    placeholder=FIELD_PLACEHOLDER_YES,
    min_length=3
)

