import os
from dotenv import load_dotenv
import psycopg2
import time
import asyncio
import asyncpg

_host="";
_database="";
_user="";
_password="";

TABLE_NAME = "BUSINESS_DATA_PYTHON_ASYNC";

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


# not working!
async def my_async_demo():
    # conn = await psycopg2.connect(host=_host,database=_database,user=_user,password=_password);   // psycopg2 is incompatible with asyncio
    uri = _user +'://'
    conn = await asyncpg.connect(user=_user, password=_password,
                                 database=_database, host=_host);
    # cursor = await conn.cursor();

    await conn.execute(CREATE_TABLE_BUSINESS_DATA);
    await conn.execute(BULK_INSERT_FROM_CSV);
    await conn.commit();
    
    await conn.close();
    pass;

asyncio.get_event_loop().run_until_complete(my_async_demo())

# if __name__ == "__main__":
#     load_env_variables();
    
#     start_bulk_insert = time.time();
    


#     end_bulk_insert = time.time();
#     dtime_bulk_insert = end_bulk_insert - start_bulk_insert;
    
#     pass
