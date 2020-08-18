import os
from dotenv import load_dotenv
import psycopg2
import time

_host="";
_database="";
_user="";
_password="";

TABLE_NAME = "BUSINESS_DATA_PYTHON";

CREATE_TABLE_BUSINESS_DATA = '''CREATE TABLE IF NOT EXISTS ''' + TABLE_NAME + ''' (
    pk BIGSERIAL PRIMARY KEY,
    CompanyName VARCHAR(500),
    EmailAddress VARCHAR(500),
    ContactFullName VARCHAR(500),
    ContactJobTitle VARCHAR(500),
    PhoneNumber VARCHAR(50),
    FaxNumber VARCHAR(100),
    Address VARCHAR(500),
    Address2 VARCHAR(500),
    Address3 VARCHAR(500),
    Town VARCHAR(500),
    County VARCHAR(500),
    Postcode VARCHAR(500),
    Region VARCHAR(500),
    Country VARCHAR(500),
    SICCode INT,
    BusinessCategory VARCHAR(500),
    WebAddress VARCHAR(500)
);'''

BULK_INSERT_FROM_CSV = '''COPY '''+TABLE_NAME+'''(
    CompanyName,EmailAddress,ContactFullName,ContactJobTitle,PhoneNumber,FaxNumber,
    Address,Address2,Address3,Town,County,Postcode,Region,Country, SICCode, 
    BusinessCategory,WebAddress) 
    FROM '/home/soumic/Codes/cloud-research-odyssey/files-n-datasets/business_data/input.csv' 
    DELIMITER '*' csv header;
'''

def load_env_variables():
    load_dotenv();
    
    _host = os.getenv("HOST");
    _database = os.getenv("DATABASE");
    _user = os.getenv("USER");
    _password = os.getenv("PASSWORD");
    
    pass

def create_connection():
    conn = None;
    try:
        # conn = psycopg2.connect(host=_host,database=_database,user=_user,password=_password);
        conn = psycopg2.connect(host=_host,database=_database,user=_user,password=_password);
    except Exception as x:
        print("Exception "+str(x));
    return conn;

def close_connection(conn):
    try:
        if conn is not None:
            conn.close()
    except Exception as x:
        print("Exception "+str(x));
    pass;

def create_cursor(conn):
    cursor = None;
    try:
        cursor = conn.cursor();
    except Exception as x:
        print("Exception "+str(x));
    return cursor;

def close_cursor(cursor):
    try:
        cursor.close();
    except Exception as x:
        print("Exception "+str(x));
    pass;


# def create_table(conn, cursor, table_sql):
#     execute_query(cursor, table_sql);
#     conn.commit();
#     pass;

# def execute_query(cursor, query):
#     cursor.execute(query);
#     pass;

def execute_query(cursor = None, query = None,conn = None, is_commit=False):
    try:
        cursor.execute(query);
        if is_commit == True:
            conn.commit();
    except Exception as x:
        print("Exception "+x);
    pass;

def fetch_query_result(cursor):
    result = cursor.fetchone();
    return result;




if __name__ == "__main__":
    load_env_variables();
    conn = create_connection();
    cursor = create_cursor(conn);

    # sql_query_test = "SELECT * FROM person;";
    # execute_query(cursor=cursor, query=sql_query_test);
    # result = fetch_query_result(cursor=cursor);
    # print("----------------------");
    # print(result);

    # create_table(conn, cursor, CREATE_TABLE_BUSINESS_DATA);
    execute_query(cursor=cursor, query=CREATE_TABLE_BUSINESS_DATA, conn=conn, is_commit=True);
    print("---------1. CREATE TABLE-------------");
    # print(result);

    print("---------2. BULK INSERT ---------------------")
    start_bulk_insert = time.time();
    
    execute_query(cursor=cursor, conn=conn, query=BULK_INSERT_FROM_CSV, is_commit=True);
    
    end_bulk_insert = time.time();
    dtime_bulk_insert = end_bulk_insert - start_bulk_insert;
    print("start_bulk_insert = "+str(start_bulk_insert));
    print("end_bulk_insert = "+str(end_bulk_insert));
    print("dtime_bulk_insert = "+str(dtime_bulk_insert));


    
    row_count_query = "SELECT COUNT(*) FROM "+TABLE_NAME+";"

    start_fetch_time = time.time();
    # ---------------------------
    execute_query(cursor=cursor, query=row_count_query);
    result = fetch_query_result(cursor=cursor);
    # ----------------------------
    end_fetch_time = time.time();
    dtime_fetch = end_fetch_time - start_fetch_time;

    print("---------3. "+row_count_query+"---------------------")
    print(result);
    print("start_fetch_time"+str(start_fetch_time));
    print("end_fetch_time"+str(end_fetch_time));
    print("dtime_fetch = "+str(dtime_fetch));
    

    close_cursor(cursor);
    close_connection(conn);

    pass
