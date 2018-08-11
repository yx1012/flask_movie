# -*- coding: utf-8 -*-

from datetime import datetime
from app import  db
#会员
class User(db.Model):
    __table_name__ = "user"
    id = db.Column(db.Integer, primary_key=True) #编号
    name = db.Column(db.String(100), unique=True) #昵称
    pwd = db.Column(db.String(100)) #密码
    email = db.Column(db.String(100), unique=True) #邮箱
    phone = db.Column(db.String(11), unique=True) #号码
    info = db.Column(db.Text) #信息
    face = db.Column(db.String(255), unique=True) #头像
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  #时间
    uuid = db.Column(db.String(255),unique=True)  #唯一标识符
    userlogs = db.relationship('Userlog', backref='user')  #外键关系关联  绑定Userlog表
    comments = db.relationship('Comment', backref='user')
    moviecols = db.relationship('Moviecol', backref='user')

    def __repr__(self):
        #描述对象的字符串
        return "<User %r>"%self.name
#会员登录日志
class Userlog(db.Model):
    __tablename__ = "userlog"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  #插入外键user.id
    ip = db.Column(db.String(100))
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow) #DateTime.UtcNow的区别UTC(协调世界时)时间
#DateTime.Now本地时间（时区不同，本地时间不同）
    def __repr__(self):
        return "<Userlog %r>"%self.id
#标签  分类
class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    movies = db.relationship('Movie',backref='tag')

    def __repr__(self):
        return  "<Tag %r>"%self.name

#电影
class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    url = db.Column(db.String(255),unique=True)
    info = db.Column(db.Text)
    logo = db.Column(db.String(255), unique=True)
    star = db.Column(db.SmallInteger)
    playnum = db.Column(db.BigInteger)
    commentnum = db.Column(db.BigInteger)
    tag_id = db.Column(db.Integer,db.ForeignKey('tag.id'))
    area = db.Column(db.String(255))
    release_time = db.Column(db.Date)
    length = db.Column(db.String(100))
    addtime = db.Column(db.String(100), index=True, default=datetime.utcnow)
    comments  = db.relationship('Comment', backref='movie')
    moviecols = db.relationship('Moviecol', backref='movie')

    def __repr__(self):
        return "<movie %r>"%self.title
#预告
class Preview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    logo = db.Column(db.String(255), unique=True)
    addtime = db.Column(db.String(100), index=True, default=datetime.utcnow)

    def __repr__(self):
        return "<Preview %r>"%self.title
#评论数据模型
class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    addtime = db.Column(db.String(100), index=True, default=datetime.utcnow)

    def __repr__(self):
        return "<Comment %r>"%self.id
#电影收藏
class Moviecol(db.Model):
    __tablename__ = 'moviecol'
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    addtime = db.Column(db.String(100), index=True, default=datetime.utcnow)

    def __repr__(self):
        return "<moviecol %r>"%self.id

#权限
class Auth(db.Model):
    __tablenam__ = 'auth'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),unique=True)
    url = db.Column(db.String(255), unique=True)
    addtime = db.Column(db.String(100), index=True, default=datetime.utcnow)

    def __repr__(self):
        return "<Auth %r>"%self.name
#角色
class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),unique=True)
    auths = db.Column(db.String(600))
    addtime = db.Column(db.String(100), index=True, default=datetime.utcnow)
    admins = db.relationship('Admin', backref='role')

    def __repr__(self):
        return "<Role %r>"%self.name

#管理员
class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 昵称
    pwd = db.Column(db.String(100))  # 密码
    is_sueper = db.Column(db.SmallInteger) #是否为超级管理员  0为超级管理员
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    addtime = db.Column(db.String(100), index=True, default=datetime.utcnow)
    adminlogs = db.relationship('Adminlog', backref='admin')  #管理员登录日志外键关联
    oplogs = db.relationship('Oplog', backref='admin')


    def __repr__(self):
        return "<Admin %r>"%self.name

#管理员登陆日志
class Adminlog(db.Model):
    __tablename__ = "adminlog"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('admin.id'))  # 插入外键user.id
    ip = db.Column(db.String(100))
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return "<Adminlog %r>"%self.id
#操作日志
class Oplog(db.Model):
    __tablename__ = "oplog"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('admin.id'))  # 插入外键user.id
    ip = db.Column(db.String(100))
    reason = db.Column(db.String(100))
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return "<Oplog %r>"%self.id

# if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    # role = Role(name='超管', auths="")
    # db.session.add(role)
    # db.session.commit()