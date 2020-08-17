import os
from dotenv import load_dotenv

var host;
var database;
var user;
var password;

def load_env_variables():
    load_dotenv();
    
    host = os.getenv("HOST");
    database = os.getenv("DATABASE");
    user = os.getenv("USER");
    password = os.getenv("PASSWORD");
    
    pass

def create_connection():
    pass;

def close_connection():

    pass;

if __name__ == "__main__":
    load_env_variables();
    pass