

#Base.metadata.create_all(engine)

#### CRUD: Create
# add_user = User('siyamak', 'abasnezhad', 'my_strong_password')
# session.add(add_user)
# session.commit()
# print(add_user.password)
# print(add_user.id)

#=====> Create Multi user
#session.add_all([
#    User('siyamak', 'abasnezhad', 'password'),
#    User('hossein', 'rafaati', 'hispassword')
#])

#session.commit()

#my_user = session.query(User).filter_by(name = 'sepehr').first()
#print(my_user)
#my_user.password = 'new_one'
#print(session.dirty)
#print(session.new)





#### CRUD: Read
#my_user = session.query(User).filter_by(name = 'sepehr').first()
#print(my_user)
#print(my_user.name)
#print(my_user.password)


#all_users = session.query(User).all()
#for user in all_users:
#    print(user.name)
#
#for my_user in session.query(User).all():
#    print(my_user)