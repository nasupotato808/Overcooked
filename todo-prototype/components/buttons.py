from interactions import Button, ButtonStyle, ActionRow
from utils.strings import *

master_row = ActionRow(
    Button(
        style=ButtonStyle.SUCCESS,
        label=TXT_ADD_TODO,
        custom_id=BTN_ADD_TODO
    ),
    Button(
        style=ButtonStyle.SECONDARY,
        label=TXT_VIEW_TODO,
        custom_id=BTN_VIEW_TODO
    )
)

todo_row_1 = ActionRow(
    Button(
        style=ButtonStyle.SUCCESS,
        label=TXT_BREAK_TODO,
        custom_id=BTN_BREAK_TODO
    ),
    Button(
        style=ButtonStyle.PRIMARY,
        label=TXT_CHECK_TODO,
        custom_id=BTN_CHECK_TODO
    ),
    Button(
        style=ButtonStyle.SECONDARY,
        label=TXT_EDIT_TODO,
        custom_id=BTN_EDIT_TODO
    ),
    Button(
        style=ButtonStyle.DANGER,
        label=TXT_DELETE_TODO,
        custom_id=BTN_DELETE_TODO
    )
)

todo_row_2 = ActionRow(
    Button(
        style=ButtonStyle.SUCCESS,
        label=TXT_ADD_STEP,
        custom_id=BTN_ADD_STEP
    ),
    Button(
        style=ButtonStyle.PRIMARY,
        label=TXT_CHECK_STEP,
        custom_id=BTN_CHECK_STEP
    ),
    Button(
        style=ButtonStyle.SECONDARY,
        label=TXT_EDIT_STEP,
        custom_id=BTN_EDIT_STEP
    ),
    Button(
        style=ButtonStyle.DANGER,
        label=TXT_DELETE_STEP,
        custom_id=BTN_DELETE_STEP
    )
)

todo_row_3 = ActionRow(
    Button(
        style=ButtonStyle.SECONDARY,
        label=TXT_BACK,
        custom_id=BTN_BACK
    )
)