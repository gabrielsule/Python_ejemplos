import sqlite3

def insert(db, row):
    db.execute('insert into test (nombre, id) values (?, ?)', (row['nombre'], row['id']))
    db.commit()

def get(db, nombre):
    cursor = db.execute('select * from test where nombre = ?', (nombre,))
    return cursor.fetchone()

def update(db, row):
    db.execute('update test set id = ? where nombre = ?', (row['id'], row['nombre']))
    db.commit()

def delete(db, nombre):
    db.execute('delete from test where nombre = ?', (nombre,))
    db.commit()

def select(db):
    cursor = db.execute('select * from test')
    for row in cursor:
        print('  {}: {}'.format(row['nombre'], row['id']))

def main():
    db = sqlite3.connect('test.db')
    db.row_factory = sqlite3.Row
    
    db.execute('drop table if exists test')
    db.execute('create table test ( nombre text, id int )')

    insert(db, dict(nombre = 'uno', id = 1))
    insert(db, dict(nombre = 'dos', id = 2))
    insert(db, dict(nombre = 'tres', id = 3))
    print('insert')
    select(db)

    update(db, dict(nombre = 'uno', id = 101))
    print('update')
    select(db)

    delete(db, 'dos')
    print('delete')
    select(db)

if __name__ == "__main__": main()
