def verify_if_exists_and_is_not_deleted(item):
    if not item or item.deleted_at:
        return False
    return True