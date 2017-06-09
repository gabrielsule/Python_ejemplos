import sqlite3

db = sqlite3.connect('test.db')

db.execute('drop table if exists test')
db.execute('create table test (id int, nombre text)')
db.execute('insert into test (id, nombre) values (?, ?)', (1, 'uno'))
db.execute('insert into test (id, nombre) values (?, ?)', (2, 'dos'))
db.execute('insert into test (id, nombre) values (?, ?)', (3, 'tres'))
db.commit()

cursor = db.execute('select * from test')
for row in cursor:
    print(row)
