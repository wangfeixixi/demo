import sqlite3

from webapp.www.orm import StringField


def init_sql(sql):
    conn = sqlite3.connect('hmi.db')
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        cursor.execute('create table car (id varchar(20) primary key, name varchar(20))')
    except Exception as e:
        print("exception:" + e)
    finally:
        cursor.close()
        conn.close()


def init_user():
    create_user = 'create table user (id varchar(%s) )' % (User)

    def next_id():
        return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

    class User(Model):
        __table__ = 'users'

        id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
        email = StringField(ddl='varchar(50)')
        passwd = StringField(ddl='varchar(50)')
        admin = BooleanField()
        name = StringField(ddl='varchar(50)')
        image = StringField(ddl='varchar(500)')
        created_at = FloatField(default=time.time)

    class Blog(Model):
        __table__ = 'blogs'

        id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
        user_id = StringField(ddl='varchar(50)')
        user_name = StringField(ddl='varchar(50)')
        user_image = StringField(ddl='varchar(500)')
        name = StringField(ddl='varchar(50)')
        summary = StringField(ddl='varchar(200)')
        content = TextField()
        created_at = FloatField(default=time.time)

    class Comment(Model):
        __table__ = 'comments'

        id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
        blog_id = StringField(ddl='varchar(50)')
        user_id = StringField(ddl='varchar(50)')
        user_name = StringField(ddl='varchar(50)')
        user_image = StringField(ddl='varchar(500)')
        content = TextField()
        created_at = FloatField(default=time.time)
D:\workspace\py\HMI\webapp\schema.sql