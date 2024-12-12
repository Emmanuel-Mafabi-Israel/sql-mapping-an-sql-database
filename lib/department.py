# GLORY BE TO GOD,
# SQL - MAPPING A PYTHON CLASS TO A DATABASE,
# BY ISRAEL MAFABI EMMANUEL

from __init__ import DB_CONNECT, CURSOR

class Department:
    def __init__(self, name:str, location:str, id:int=None)->None:
        self.name     = name
        self.location = location
        self.id       = id

    @classmethod
    def create_table(cls)->None:
        # function for creating the table...
        # DEPARTMENTS TABLE...
        SQL = """
            CREATE TABLE IF NOT EXISTS departments (
                id INTEGER PRIMARY KEY,
                name TEXT UNIQUE,
                location TEXT
            );
        """
        try :
            CURSOR.execute(SQL)
            DB_CONNECT.commit()
            print("Created departments table succesfully!")
        except Exception as e:
            print(f"An error occurred while creating the table: {e}")

    @classmethod
    def drop_table(cls)->None:
        # function for dropping the table...
        # DEPARTMENTS TABLE...
        SQL = """
            DROP TABLE IF EXISTS departments;
        """
        try:
            CURSOR.execute(SQL)
            DB_CONNECT.commit()
            print("Dropped departments table succesfully!")
        except Exception as e:
            print(f"An error occurred while dropping the table: {e}")

    @classmethod
    def create(cls, name:str, location:str):
        # initializing a new department instance and save the object to database...
        department:Department = cls(name, location)
        department.save_data()
        return department

    def __repr__(self)->str:
        return f"<Department {self.id}: {self.name}, {self.location}>"
    
    def save_data(self):
        # inserting a new row with the name and location values of the current
        # department's instance...
        SQL = """
            INSERT INTO departments (name, location)
            VALUES (?, ?)
        """
        try:
            CURSOR.execute(SQL, (self.name, self.location))
            DB_CONNECT.commit()

            self.id = CURSOR.lastrowid # -> generate a new id based from the last one...
            print(f"Inserted row(department's instance: {self.name}) into departments table succesfully!")
        except Exception as e:
            print(f"An error occurred while inserting into the table: {e}")

    def update_data(self):
        # update the table row corresponding to the current department's instance...
        SQL = """
            UPDATE departments
            SET name = ?, location = ?
            WHERE id = ?
        """
        try:
            CURSOR.execute(SQL, (self.name, self.location, self.id))
            DB_CONNECT.commit()

            print(f"Updated row(department's instance: {self.name}) in departments table succesfully!")
        except Exception as e:
            print(f"An error occurred while updating the table record: {e}")

    def delete_data(self):
        # delete the table row corresponding to the current department's instance...
        SQL = """
            DELETE FROM departments
            WHERE id = ?
        """
        try:
            CURSOR.execute(SQL, (self.id,))
            DB_CONNECT.commit()

            print(f"Deleted row(department's instance: {self.name}) in departments table succesfully!")
        except Exception as e:
            print(f"An error occurred while deleting the table record: {e}")

# Department.create_table()
# Department.drop_table()