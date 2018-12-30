

#for instance in session.query(User).order_by(User.id):
#    print(instance.name)


#for name, fullname in session.query(User.name, User.fullname):
#    print(name, fullname)

#for row in session.query(User, User.name).all():
#    print(row.User, row.name)

#for row in session.query(User.name.label('name_label')).all():
#    print(row.name_label)

#user_aliase = aliased(User, name='user_aliase')
#for row in session.query(user_aliase, user_aliase.name).all():
#    print(row.user_aliase)

#for row in session.query(User).order_by(User.id)[0:3]:
#    print(row)

#for name in session.query(User.name).filter_by(fullname = 'sepehr'):
#    print(name)

#for name in session.query(User.name).filter(User.fullname == 'akbarzadeh'):
#    print(name)

#for user in session.query(User).\
#    filter(User.name == 'sepehr').\
#    filter(User.fullname == 'akbarzadeh'):
#    print(user)



#for user in session.query(User).filter(User.name == 'sepehr'):
#    print(user)
#
#for user in session.query(User).filter(User.name != 'sepehr'):
#    print(user)

#for user in session.query(User).filter(User.password.like('%pass%')):
#    print(user)

#for user in session.query(User).filter(User.name.in_(['siyamak', 'saeed', 'majid'])):
#    print(user)

# for user in session.query(User).filter(~User.name.in_(['diyana', 'sami', 'majid'])):
#        print(user)

#for user in session.query(User).filter(User.name != None):
#    print(user)

#for user in session.query(User).filter(and_(User.name != None, User.password == 'password')):
#    print(user)
#
#for user in session.query(User).filter(or_(User.name != None, User.password == '1234')):
#    print(user)
#

# for user in session.query(User).from_statement(r"SELECT * FROM users WHERE name=:name").params(name='siyamak').all():
#        print(user)