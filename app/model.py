import logging
import time
import mysql.connector
import os

logger = logging.getLogger(__name__)


def setup():
    config = {
        'host': os.getenv("MYSQL_HOST"),
        'user': os.getenv("MYSQL_USER"),
        'passwd': os.getenv("MYSQL_PASSWORD"),
        'database': os.getenv("MYSQL_DATABASE")
    }
    return config

def getconn():
    config = setup()
    retries = 5
    while retries:
        try:
            mydb = mysql.connector.connect(**config)
            return mydb
        except :
            retries -= 1
            logger.error("Connection failed.. Retrying after 1 sec")
            time.sleep(1)



def getdbs():
    mydb = getconn()
    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS wonderkidz")
    mycursor.execute("CREATE TABLE IF NOT EXISTS `EMPLOYEES` (`id` INT AUTO_INCREMENT PRIMARY KEY, `name` VARCHAR(255), `address` VARCHAR(255))")
    mycursor.execute("SHOW DATABASES;")
    dbs = mycursor.fetchall()
    dbs = [x[0] for x in dbs]
    mydb.close()
    return dbs

def get_emp_list():
    mydb = getconn()
    mycursor = mydb.cursor()
    mycursor.execute("select * from wonderkidz.EMPLOYEES;")
    dbs = mycursor.fetchall()
    dbs = [x[0] for x in dbs]
    mydb.close()
    return dbs