from sqlalchemy import create_engine, text
import pytest
from DataBase import DataBase

db_connection_string = "postgresql://catherine:12345Katrin@localhost:5433/mydatabase"


def test_table_teacher():
    database = DataBase(db_connection_string) 
     
    database.insert_teacher(55555, 'myteacher@gmail.com', 55)

    rows = database.select_teacher(55555)
    assert len(rows) > 0  # Проверяем, что мы получили одну запись
    assert rows[-1].teacher_id == 55555  # Проверяем, что ID совпадает
    assert rows[-1].email == 'myteacher@gmail.com'  # Проверяем, что email совпадает
    assert rows[-1].group_id == 55  # Проверяем, что group_id совпадает

    database.update_teacher(55555, 'updated_email@gmail.com', 11)
    updated_rows = database.select_teacher(55555)
    assert len(updated_rows) > 0  # Проверяем, что мы все еще получаем одну запись
    assert updated_rows[-1].email == 'updated_email@gmail.com'  # Проверяем, что email был обновлен
    assert updated_rows[-1].group_id == 11  # Проверяем, что group_id был обновлен

    # Тест для удаления
    database.delete_teacher(55555)
    deleted_rows = database.select_teacher(55555)
    assert len(deleted_rows) == 0  # Проверяем, что записи больше нет

