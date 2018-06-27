#!/usr/bin/env python3

from datetime import datetime
from model import db, User, Task
from passlib.hash import pbkdf2_sha256


# Recreate DB
db.connect()
db.drop_tables([User, Task])
db.create_tables([User, Task])

# Prepopulate sample users
User(name="admin", password=pbkdf2_sha256.hash("password")).save()
User(name="bob", password=pbkdf2_sha256.hash("bobbob")).save()

# Prepopulate sample tasks
Task(name="Do the laundry.").save()
Task(name="Do the dishes.", performed=datetime.now()).save()

