import psycopg2

def read_db():
    conn= psycopg2.connect(dbname='epamproject',user='postgres',
                           password='18101996Paul',host='localhost')

    cursor = conn.cursor()
    cursor.execute('select site_name from public.parser_data')
    rec= cursor.fetchall()
    cursor.close()
    conn.close
    return rec

def write_db (site,url,tags):
    conn = psycopg2.connect(dbname='epamproject', user='postgres',
                            password='18101996Paul', host='localhost')
    cursor = conn.cursor()
    cursor.execute('insert into public.parser_data(site_name,url,check_date,tags_data) '
                   'values (\''+site+'\',\''+url+'\',now(),\''+str(tags).replace('\'','\"',100000)+'\');')
    cursor.execute('commit;')
    cursor.close()
    conn.close
