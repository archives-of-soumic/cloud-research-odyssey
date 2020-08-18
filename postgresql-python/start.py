import os
from dotenv import load_dotenv
import psycopg2

_host="";
_database="";
_user="";
_password="";

CREATE_TABLE_BUSINESS_DATA = '''CREATE TABLE IF NOT EXISTS BUSINESS_DATA (
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


def insert_prototype():

    pass;

if __name__ == "__main__":
    load_env_variables();
    conn = create_connection();
    cursor = create_cursor(conn);

    sql_query_test = "SELECT * FROM person;";
    execute_query(cursor=cursor, query=sql_query_test);
    result = fetch_query_result(cursor=cursor);
    print("----------------------");
    print(result);

    # create_table(conn, cursor, CREATE_TABLE_BUSINESS_DATA);
    execute_query(cursor=cursor, query=CREATE_TABLE_BUSINESS_DATA, conn=conn, is_commit=True);
    print("---------1. CREATE TABLE-------------");
    # print(result);

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
    close_cursor(cursor);
    close_connection(conn);

    pass
