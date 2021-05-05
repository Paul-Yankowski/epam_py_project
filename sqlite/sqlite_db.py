import sqlite3
connection = sqlite3.connect("epam_project.db")
#(":memory:")
#("epam_project.db")
sql = connection.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS tags_data (
    site_name text,
    url text,
    check_date text,
    tags_info text)
    """)

def read_db():
    sql.execute("select * from tags_data")
    rec = sql.fetchall()
    return rec

def write_db (site,url,tags):
    sql.execute('insert into tags_data(site_name,url,tags_info) '
                   'values (\''+site+'\',\''+url+'\',\''+str(tags).replace('\'','\"',100000)+'\');')
    connection.commit()