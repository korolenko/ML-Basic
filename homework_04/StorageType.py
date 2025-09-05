from enum import Enum
class StorageType(Enum):
    LOCAL = 'local'
    S3 = 's3'
    REMOTE_SERVER = 'remote server'