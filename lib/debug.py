# GLORY BE TO GOD,
# SQL - MAPPING A PYTHON CLASS TO A DATABASE,
# DEBUGGING FILE...
# BY ISRAEL MAFABI EMMANUEL

from __init__ import DB_CONNECT, CURSOR
from department import Department

import ipdb

Department.drop_table()
Department.create_table()

payroll:Department = Department.create("Payroll", "Building A, 5th Floor")
print(payroll) # <Department None: Payroll, Building A, 5th Floor>

human_resource:Department = Department.create("Human Resource", "Building C, East Wing")
print(human_resource)

# Trying the update and delete functionality...
# UPDATE
human_resource.name = "HR"
human_resource.location = "Building F, 10th Floor"
human_resource.update_data()

# DELETE
payroll.delete_data()

ipdb.set_trace()