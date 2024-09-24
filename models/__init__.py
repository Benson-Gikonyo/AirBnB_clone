#!/usr/bin/env python3
""" Initialization file"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


storage = FileStorage()
storage.reload()
