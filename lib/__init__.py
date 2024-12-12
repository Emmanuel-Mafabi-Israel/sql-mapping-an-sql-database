# GLORY BE TO GOD,
# SQL - MAPPING A PYTHON CLASS TO A DATABASE,
# CONFIG - INITIALIZATION FILE...
# BY ISRAEL MAFABI EMMANUEL

import os
import sqlite3

# Get the directory where the department.py file is in...
BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
DB_FOLDER  = os.path.join(BASE_DIR, 'database')
# optional... create the db folder if it does not exist
if not os.path.exists(DB_FOLDER):
    os.makedirs(DB_FOLDER)
DB_PATH    = os.path.join(DB_FOLDER, 'company.db')

DB_CONNECT = sqlite3.connect(DB_PATH)
CURSOR     = DB_CONNECT.cursor()