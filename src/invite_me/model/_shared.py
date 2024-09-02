import uuid_extensions
from sqlalchemy import Column, UUID


def id_col():
    """
    To ensure all columns with uuids are created as uuid7.

    uuid7 is sorted, and will play better with the db indexes than non-sorted uuids.
    :return:
        sqlalchemy.Column: Column configured to be a primary key and of type uuid7
    """
    return Column(UUID, primary_key=True, default=uuid_extensions.uuid7())
