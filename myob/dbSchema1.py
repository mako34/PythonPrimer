#!/usr/bin/python3

# sqlite3-class.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

import sqlite3

#ojo es una clase!
class database:

    #el init!
    def __init__(self, **kwargs): #q es kwargs
        print ('el init de la clase')
        self.filename = kwargs.get('filename')
        self.table = kwargs.get('table', 'Employee')
    
    #las funciones en clase!
    def sql_do(self, sql, *params):
        self._db.execute(sql, params)
        self._db.commit()
    
    def insert(self, row):
        self._db.execute('insert into {} (name, surname) values (?, ?)'.format(self._table), (row['name'], row['surname']))
        self._db.commit()
    
    def retrieve(self, key):
        cursor = self._db.execute('select * from {} where name = ?'.format(self._table), (key,))
        return dict(cursor.fetchone())
    
    def update(self, row):
        self._db.execute(
            'update {} set surname = ? where name = ?'.format(self._table),
            (row['surname'], row['name']))
        self._db.commit()
    
    def delete(self, key):
        self._db.execute('delete from {} where name = ?'.format(self._table), (key,))
        self._db.commit()

    def disp_rows(self):
        cursor = self._db.execute('select * from {} order by name'.format(self._table))
        for row in cursor:
            print('  {}: {}'.format(row['name'], row['surname']))

    def __iter__(self):
        cursor = self._db.execute('select * from {} order by name'.format(self._table))
        for row in cursor:
            yield dict(row)


    #entender este pedazo!
    @property
    def filename(self): return self._filename

    @filename.setter
    def filename(self, fn):
        self._filename = fn
        self._db = sqlite3.connect(fn)
        self._db.row_factory = sqlite3.Row

    @filename.deleter
    def filename(self): self.close()

    @property
    def table(self): return self._table
    @table.setter
    def table(self, t): self._table = t
    @table.deleter
    def table(self): self._table = 'Employee'

    def close(self):
            self._db.close()
            del self._filename

def main():
    print('el main')
    #como llamo varios clases?

    db = database(filename = 'timeSheets.db', table = 'Employee')

    print('Create table Employee')
    db.sql_do('drop table if exists Employee')
    db.sql_do('create table Employee ( name text, surname int )')

    print('Create rows')
    db.insert(dict(name = 'one', surname = 1))
    db.insert(dict(name = 'two', surname = 2))
    db.insert(dict(name = 'three', surname = 3))
    db.insert(dict(name = 'four', surname = 4))
    for row in db: print(row)

    print('Retrieve rows')
    print(db.retrieve('one'), db.retrieve('two'))

    print('Update rows')
    db.update(dict(name = 'one', surname = 101))
    db.update(dict(name = 'three', surname = 103))
    for row in db: print(row)

    print('Delete rows')
    db.delete('one')
    db.delete('three')
    for row in db: print(row)

#esta la vuelve corrible desde afuera
if __name__ == "__main__": main()
