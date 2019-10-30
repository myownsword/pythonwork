from www.orm import Model, StringField, IntegerField

class User(Model):
    __table__ = 'user'

    id = IntegerField(primary_key=True)
    name = StringField()

# # 创建实例:
# user = User(id=123, name='Michael2')
# # 存入数据库:
# # user.update(user)
# # 查询所有User对象:
# users = User.findAll()

# u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# u.save()


