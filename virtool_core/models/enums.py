from enum import Enum


class Permission(Enum):
    cancel_job = "cancel_job"
    create_ref = "create_ref"
    create_sample = "create_sample"
    modify_hmm = "modify_hmm"
    modify_subtraction = "modify_subtraction"
    remove_file = "remove_file"
    remove_job = "remove_job"
    upload_file = "upload_file"


class HistoryMethod(Enum):
    add_isolate = "add_isolate"
    clone = "clone"
    create_sequence = "create_sequence"
    create = "create"
    edit = "edit"
    edit_isolate = "edit_isolate"
    edit_sequence = "edit_sequence"
    import_otu = "import"
    remove = "remove"
    remove_isolate = "remove_isolate"
    remove_sequence = "remove_sequence"
    remote = "remote"
    set_as_default = "set_as_default"
    update = "update"
