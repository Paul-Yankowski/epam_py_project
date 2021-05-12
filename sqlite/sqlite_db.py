import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("epam_project.db")
        self.connection.cursor().execute("""CREATE TABLE IF NOT EXISTS tags_data (
                            site_name text,
                            url text,
                            check_date text,
                            tags_info text)
                            """)


    def read_db(self):
        sql = self.connection.cursor()
        sql.execute("select * from tags_data")
        rec = sql.fetchall()
        return rec

    def write_db(self,obj):
        sql = self.connection.cursor()
        sql.execute('insert into tags_data(site_name,url,tags_info) '
                    'values (\'' + obj.site_name + '\',\'' + obj.URL + '\',\'' + str(obj.tags()).replace('\'', '\"', 100000) + '\');')
        self.connection.commit()
