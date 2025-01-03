from interactions import Modal
from utils.strings import *
from .modal_fields import *

def create_modal(title: str, custom_id: str, *fields):
    return Modal(
        fields,
        title=title,
        custom_id=custom_id
    )

modal_add_todo = create_modal(
    TXT_ADD_TODO,
    MOD_ADD_TODO,
    field_description)

modal_add_step = create_modal(
    TXT_ADD_STEP,
    MOD_ADD_STEP,
    field_description)

modal_check_step = create_modal(
    TXT_CHECK_STEP,
    MOD_CHECK_STEP,
    field_step_id
)

modal_edit_todo = create_modal(
    TXT_EDIT_TODO,
    MOD_EDIT_TODO,
    field_description
)

modal_edit_step = create_modal(
    TXT_EDIT_STEP,
    MOD_EDIT_STEP,
    field_step_id,
    field_description
)

modal_delete_todo = create_modal(
    TXT_DELETE_TODO,
    MOD_DELETE_TODO,
    field_confirm_delete
)

modal_delete_step = create_modal(
    TXT_DELETE_STEP,
    MOD_DELETE_STEP,
    field_step_id,
    field_confirm_delete
)