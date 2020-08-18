# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Postgresql Tests With Python
# In this jupyter notebook, I will be testing bulk insert, execute some queries on about 2 million rows of data, and save their execution times.
# %% [markdown]
# ## Import libraries

# %%
import os
from dotenv import load_dotenv
import psycopg2
import time

# %% [markdown]
# ## Declare Variables and SQL Commands

# %%
_host="";
_database="";
_user="";
_password="";

TABLE_NAME = "BUSINESS_DATA_JUPYTER";

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
);''';

BULK_INSERT_FROM_CSV = '''COPY '''+TABLE_NAME+'''(
    CompanyName,EmailAddress,ContactFullName,ContactJobTitle,PhoneNumber,FaxNumber,
    Address,Address2,Address3,Town,County,Postcode,Region,Country, SICCode, 
    BusinessCategory,WebAddress) 
    FROM '/home/soumic/Codes/cloud-research-odyssey/files-n-datasets/business_data/input.csv' 
    DELIMITER '*' csv header;
''';

QUERY_1 = '''SELECT COUNT(*) FROM '''+TABLE_NAME+'''WHERE EmailAddress LIKE '%.com';''';
QUERY_DELETE = '''DELETE FROM '''+TABLE_NAME + ''' WHERE PK&1 == 1;''';
QUERY_DROP = '''DROP TABLE '''+TABLE_NAME+''';''';

# %% [markdown]
# ## Load Credentials From .Env File

# %%
def load_env_variables():
    load_dotenv();
    
    _host = os.getenv("HOST");
    _database = os.getenv("DATABASE");
    _user = os.getenv("USER");
    _password = os.getenv("PASSWORD");
    
    pass

# %% [markdown]
# ## Create and Close Connections
# I'll define some functions that will connect us to postgresql. When work is finished, we should close the connections:

# %%
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

# %% [markdown]
# ## Main Function Start
# 

# %%
# if __name__ == "__main__":
load_env_variables();
conn = create_connection();
cursor = create_cursor(conn);

# %% [markdown]
# ## Create Table

# %%
print("---------1. CREATE TABLE-------------");
start_time1 = time.time();

cursor.query(CREATE_TABLE_BUSINESS_DATA);
conn.commit();

end_time1 = time.time();
dt1 = end_time1 - start_time1;
print("Time to create table = "+dt1);

# %% [markdown]
# ### Output
# 
# ## InsertData

# %%
print("---------2. BULK INSERT ---------------------")
start_bulk_insert = time.time();

# execute_query(cursor=cursor, conn=conn, query=BULK_INSERT_FROM_CSV, is_commit=True);
cursor.query(BULK_INSERT_FROM_CSV);
conn.commit(True);

end_bulk_insert = time.time();
dtime_bulk_insert = end_bulk_insert - start_bulk_insert;

print("start_bulk_insert = "+str(start_bulk_insert));
print("end_bulk_insert = "+str(end_bulk_insert));
print("dtime_bulk_insert = "+str(dtime_bulk_insert));

# %% [markdown]
# ### Output
# ## Execute Some Simple Queries

# %%
print("---------3. SIMPLE QUERIES ---------------------")
start_3 = time.time();

# execute_query(cursor=cursor, conn=conn, query=BULK_INSERT_FROM_CSV, is_commit=True);
cursor.query(QUERY_1);
result = cursor.fetchone();

end_3 = time.time();
dtime_3 = end_3 - start_3;

print("start_3 = "+str(start_3));
print("end_3 = "+str(end_3));
print("dtime_3 = "+str(dtime_3));

# %% [markdown]
# ### Output
# ## Delete 50% Data Like Thanos :fire:

# %%
print("---------4. DELETE DATA ---------------------")
start_4 = time.time();

# execute_query(cursor=cursor, conn=conn, query=BULK_INSERT_FROM_CSV, is_commit=True);
cursor.query(QUERY_DELETE);
result = cursor.fetchone();

end_4 = time.time();
dtime_4 = end_4 - start_4;

print("start_4 = "+str(start_4));
print("end_4 = "+str(end_4));
print("dtime_4 = "+str(dtime_4));

# %% [markdown]
# ### Output
# ## Drop Table

# %%
print("---------5. DROP TABLE ---------------------")
start_5 = time.time();

# execute_query(cursor=cursor, conn=conn, query=BULK_INSERT_FROM_CSV, is_commit=True);
cursor.query(QUERY_DELETE);
conn.commit();

end_5 = time.time();
dtime_5 = end_5 - start_5;

print("start_5 = "+str(start_5));
print("end_5 = "+str(end_5));
print("dtime_5 = "+str(dtime_5));

# %% [markdown]
# ### Output
# ## Close Connections

# %%
close_cursor(cursor);
close_connection(conn);

# pass

# %% [markdown]
# 

