from sqlmodel import SQLModel, create_engine;

url = 'mysql+pymysql://root:toor@localhost:3306/test'
engine = create_engine(url, echo=True)

SQLModel.metadata.create_all(engine)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)