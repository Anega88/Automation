from sqlalchemy import create_engine, text


class DataBase:

    def __init__(self, db_connection_string):
        self.db = create_engine(db_connection_string)

    def insert_teacher(self, teacher_id, email, group_id):
        with self.db.connect() as connection:
            sql = text("INSERT INTO teacher(teacher_id, email, group_id) VALUES (:new_teacher_id, :new_email, :new_group_id)")
            connection.execute(sql, {
                'new_teacher_id': teacher_id,
                'new_email': email,
                'new_group_id': group_id
                })
            connection.commit()

    def select_teacher(self, teacher_id):
        with self.db.connect() as connection:
            sql = text("SELECT * FROM teacher WHERE teacher_id = :new_teacher_id")
            result = connection.execute(sql, {
                'new_teacher_id': teacher_id,
            })
            return result.fetchall()
    
    def update_teacher(self, teacher_id, email, group_id):        
        with self.db.connect() as connection:
            sql = text("UPDATE teacher SET group_id = :new_group_id, email = :new_email WHERE teacher_id = :new_teacher_id")
            connection.execute(sql, {
                'new_teacher_id': teacher_id,
                'new_email': email,
                'new_group_id': group_id
                })
            connection.commit()
            
    def delete_teacher(self, teacher_id):  
        with self.db.connect() as connection:
            sql = text("DELETE FROM teacher WHERE teacher_id = :old_teacher_id")
            connection.execute(sql, {
                'old_teacher_id': teacher_id,
                })
            connection.commit()

if __name__ == "__main__":
    db_connection_string = "postgresql://catherine:12345Katrin@localhost:5433/mydatabase"
    db = DataBase(db_connection_string)
    db.insert_teacher(55555, 'myteacher@gmail.com', 55)
