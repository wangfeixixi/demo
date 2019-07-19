from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from webapp.www.model import User

engine = create_engine('sqlite:///dd.db?check_same_thread=False', echo=True)

Base = declarative_base()

# class User(Base):
#     __tablename__ = 'users'
#
#     id = Column(Integer, primary_key=True)
#     email = Column(String(50))
#     # passwd = Column(String(50))
#     # admin = Column(Boolean())
#     name = Column(String(50))
#
#     # image = Column(String(500))
#     # created_at = Column(Float(time.time))
#
#     def __repr__(self):
#         return "<User(name='%s', fullname='%s')>" % (
#             self.name, self.email,)
#
#
# class Blog(Base):
#     __tablename__ = 'blogs'
#
#     id = Column(Integer, primary_key=True)
#     user_id = Column(String(50))
#     user_name = Column(String(50))
#     user_image = Column(String(500))
#     name = Column(String(50))
#     summary = Column(String(200))
#     content = Column(Text())
#     created_at = Column(Float(time.time))
#
#
# class Comment(Base):
#     __tablename__ = 'comments'
#
#     id = Column(Integer, primary_key=True)
#     blog_id = Column(String(50))
#     user_id = Column(String(50))
#     user_name = Column(String(50))
#     user_image = Column(String(500))
#     content = Column(Text())
#     created_at = Column(Float(time.time))


# 创建数据表
Base.metadata.create_all(engine)

# engine是2.2中创建的连接
Session = sessionmaker(bind=engine)

# 创建Session类实例
session = Session()

# 创建User类实例
ed_user = User(name='ed', email="email")
# ed_user = User(name='ed', email="email", passwd="passwd", admin=False,image = "image")

# 将该实例插入到users表
session.add(ed_user)

# 一次插入多条记录形式
# session.add_all(
# [User(name='wendy', email='Wendy Williams', passwd='foobar'),
#  User(name='mary', email='Mary Contrary', passwd='xxg527'),
#  User(name='fred', email='Fred Flinstone', passwd='blah')]
# )

# 当前更改只是在session中，需要使用commit确认更改才会写入数据库
session.commit()

# 指定User类查询users表，查找name为'ed'的第一条数据
our_user = session.query(User).filter_by(name='ed').first()
our_user2 = session.query(User).filter_by(name='wendy').first()
filter_all = session.query(User).filter_by()

# print('------------'+our_user)
print(our_user)
print(filter_all)

