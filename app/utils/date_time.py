from datetime import datetime, timezone


def generate_datetime_now():
    return datetime.now(tz=timezone.utc)
