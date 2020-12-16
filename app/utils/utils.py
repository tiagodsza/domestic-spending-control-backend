from uuid import UUID

def verify_if_exists_and_is_not_deleted(item):
    if not item or item.deleted_at:
        return False
    return True

def is_empty(value: str):
    if len(value.strip()) == 0:
        return True
    return False

def is_valid_uuid(value: str):
    try:
        UUID(value, version=4)
        return True
    except ValueError:
        return False
