from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from .config import settings

SQLALCHEMY_DATABASE_URL = URL.create(
    drivername="postgresql",
    username=settings.db_username,
    password=settings.db_password,
    host=settings.db_hostname,
    port=settings.db_port,
    database=settings.db_name
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Database Connection, not need anymore but code preseved ==========================
# while True:
#     try:
#         conn = psycopg2.connect( 
#             host = 'localhost', 
#             database='fastapi', 
#             user='postgres', 
#             password = 'p@ssw0rd', 
#             cursor_factory=RealDictCursor )
#         cursor  = conn.cursor()
#         print(" oooooooooooooooooooooooooooo Database Connected oooooooooooooooooooooooooooo")
#         break
#     except Exception as error:
#         print(" xxxxxxxxxxxxxxxxxxxxxxxxx Database connection failed xxxxxxxxxxxxxxxxxxxxxxxxx")
#         print("Error:" , error)
#         time.sleep(2)