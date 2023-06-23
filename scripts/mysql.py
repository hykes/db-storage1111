import pymysql


class Mysql(object):
    def __init__(self):
        self._connect = pymysql.connect(
            host='127.0.0.1',
            user='test',
            password='######',
            database='test',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        self._cursor = self._connect.cursor()

    def inset_db(self, table_name, insert_data):
        try:
            data = self.get_mysql_data(data=insert_data)
            fields = data[0]
            values = data[1]
            sql = "INSERT INTO {table_name}({fields}) values ({values})".format(table_name=table_name, fields=fields,
                                                                                values=values)
            self._cursor.execute(sql)
            self._connect.commit()
        except Exception as e:
            self._connect.rollback()  # 如果这里是执行的执行存储过程的sql命令，那么可能会存在rollback的情况，所以这里应该考虑到
            print("数据插入失败，失败原因:", e)
            print(insert_data)
        else:
            # self.db_close()
            return self._cursor.lastrowid

    def update_db(self, table_name, update_data, wheres=None):
        try:
            if wheres is not None:
                sql = "UPDATE {table_name} SET {update_data} WHERE {wheres}".format(
                    table_name=table_name,
                    update_data=update_data,
                    wheres=wheres
                )
            else:
                sql = "UPDATE {table_name} SET {update_data}".format(
                    table_name=table_name,
                    update_data=update_data)
            self._cursor.execute(sql)
            self._connect.commit()
        except Exception as e:
            print("更新失败:", e)
            return False
        else:
            # self.db_close()
            return True

    def delete_db(self, table_name, wheres):
        try:
            # 构建sql语句
            sql = "DELETE FROM {table_name} WHERE {wheres}".format(table_name=table_name, wheres=wheres)
            self._cursor.execute(sql)
            self._connect.commit()
        except Exception as e:
            print('删除失败：', e)
            return False
        else:
            # self.db_close()
            return True

    def select_db(self, table_name, fields, wheres=None, get_one=False):
        try:
            if wheres is not None:
                sql = "SELECT {fields} FROM {table_name} WHERE {wheres}".format(
                    fields=fields,
                    table_name=table_name,
                    wheres=wheres
                )
            else:
                sql = "SELECT {fields} FROM {table_name}".format(fields=fields, table_name=table_name)
            self._cursor.execute(sql)
            self._connect.commit()
            if get_one:
                result = self._cursor.fetchone()
            else:
                result = self._cursor.fetchall()
        except Exception as e:
            print("查询失败", e)
            return None
        else:
            # self.db_close()
            return result

    def get_mysql_data(self, data):
        fields = ""
        insert_data = ""
        for k, v in data.items():
            fields = fields + k + ','
            insert_data = insert_data + "'" + str(v) + "'" + ','
        fields = fields.strip(',')
        insert_data = insert_data.strip(',')
        return [fields, insert_data]

    def db_close(self):
        self._cursor.close()
        self._connect.close()