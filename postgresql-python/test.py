#!/usr/bin/python
import psycopg2

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
                host="localhost",
                database="admindb",
                user="admindb",
                password="fake_password")
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def insert_prototype(conn, cursor):
    # ------------ INSERT PROTOTYPE ------------

    data1 = '''Arlesey Carpet Warehouse,foord.hoffer@arleseycarpets.co.uk,Foord Hoffer,Principal,01462-733350,,Ram Yard,High Street,,Arlesey,Bedfordshire,SG15 6SW,Eastern,England,51471,Housewares,www.arleseycarpets.co.uk'''
    data2 = '''Arlesey Bicycle Company,struzenski.hassan@rjmclassic.com,Struzenski Hassan,Partner,01462-835970,,Ram Yard,High Street,,Arlesey,Bedfordshire,SG15 6SW,Eastern,England,50400,"Recreational Vehicle, Motorcycle & Boat Retail",www.rjmclassic.com'''
    header = '''CompanyName,EmailAddress,ContactFullName,ContactJobTitle,PhoneNumber,FaxNumber,Address,Address2,Address3,Town,County,Postcode,Region,Country,SICCode,BusinessCategory,WebAddress'''
    # 0 based e 14
    args1 = [];
    args2 = [];
    headers = [];

    args1 = data1.split(",");
    args2 = data2.split(",");
    headers = header.split(",");

    Insert_prefix = "INSERT INTO business_data ("+header+") VALUES (";
    Insert_suffix = ");";

    i = -1;
    insert_values = "";
    for v in args1:
        i=i+1;
        if(i == 14):
            insert_values = insert_values + v + ",";
        elif(i == 16):
            insert_values = insert_values +"'"+v+"'";
        else:
            insert_values = insert_values +"'"+v+"',";
    
    sql_insert = Insert_prefix + insert_values + Insert_suffix;

    execute_query(cursor=cursor, query=sql_insert, conn=conn, is_commit=True);

    execute_query(cursor=cursor, query="select * from business_data;");
    result = fetch_query_result(cursor=cursor);
    print(result);
    # ------------------------------------------
    pass;


if __name__ == '__main__':
    connect()

#     ---------1. CREATE TABLE-------------
# start_bulk_insert = 1597764497.665616
# end_bulk_insert = 1597764525.7351696
# dtime_bulk_insert = 28.06955361366272
# ---------2. SELECT COUNT(*) FROM BUSINESS_DATA_PYTHON;---------------------
# (2226295,)
# start_fetch_time1597764525.7352195
# end_fetch_time1597764526.2405286
# dtime_fetch = 0.5053091049194336