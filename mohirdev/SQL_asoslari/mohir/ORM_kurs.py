from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Declarative base class yaratish
Base = declarative_base()

# User sinfi - bu users jadvalining ORM modeli
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    familya = Column(String)
    email = Column(String)

# PostgreSQL ma'lumotlar bazasiga ulanish
engine = create_engine('postgresql://shohruh:Shoh1221web@localhost:5432/contact_db')

# Ma'lumotlar bazasida jadval yaratish
Base.metadata.create_all(engine)

# Session yaratish
Session = sessionmaker(bind=engine)
session = Session()

# Yangi foydalanuvchi qo'shish
new_user = User(name='Shohruh', familya='Egamov', email='shohruh@example.com')
session.add(new_user)
session.commit()

# Qo'shilgan foydalanuvchini ko'rish
users = session.query(User).all()
for user in users:
    print(user.name, user.familya, user.email)
