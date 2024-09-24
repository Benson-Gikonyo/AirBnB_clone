#!/usr/bin/env python3
""" Initialization file"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


storage = FileStorage()
storage.reload()
