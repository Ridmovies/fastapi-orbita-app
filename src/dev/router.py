import os

from fastapi import APIRouter
from sqlalchemy import text

from src.database import SessionDep, engine
from src.dev.utils import fill_database_utils
from src.models import Base


router = APIRouter()

@router.get("")
async def root():
    return {"message": "Hello World"}


@router.delete("/drop_db")
async def drop_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        # Удаляем таблицу alembic_version
        await conn.execute(text("DROP TABLE IF EXISTS alembic_version"))
        await conn.run_sync(Base.metadata.create_all)
    return {"message": "Database dropped"}


@router.delete("/drop_sqlite")
async def drop_sqlite():
    """Delete the sqlite database file"""
    file_path = os.path.join(os.getcwd(), "database.db")
    try:
        os.remove(file_path)
    except OSError as e:
        print(f"Ошибка при удалении файла: {e.strerror}")

    # Указываем путь к папке, где находятся файлы
    folder_path = os.path.join(os.getcwd(), "alembic/versions")

    # Получаем список всех файлов и подкаталогов в этой папке
    files_and_folders = os.listdir(folder_path)

    for file in files_and_folders:
        # Формируем полный путь к каждому файлу/папке
        full_path = os.path.join(folder_path, file)

        # Проверяем, является ли объект файлом
        if os.path.isfile(full_path):
            try:
                # Удаляем файл
                os.remove(full_path)
                print(f'Файл {full_path} успешно удален.')
            except OSError as e:
                print(f'Не удалось удалить файл {full_path}: {e.strerror}')
    #
    return {"message": "Sqlite database dropped"}


@router.get("/check-db-connection")
async def check_db_connection(session: SessionDep):
    """Check if the database connection is successful"""
    await session.execute(text("SELECT 1"))
    return {"message": "Connection to the database successful"}


@router.post("/fill_database")
async def fill_database(session: SessionDep):
    """Fill the database with test data"""
    await fill_database_utils(session=session)
    return {"message": "Database filled with test data"}



