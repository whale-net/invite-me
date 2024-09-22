import uuid_extensions
from sqlmodel import Field

import datetime as dt


def id_col():
    """
    To ensure all columns with uuids are created as uuid7.

    uuid7 is sorted, and will play better with the db indexes than non-sorted uuids.
    :return:
        sqlmodel.Field: Column configured to be a primary key and of type uuid7
    """
    return Field(primary_key=True, default=uuid_extensions.uuid7())


def created_updated_col():
    return Field(default=dt.datetime.now(dt.UTC))
