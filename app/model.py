import logging

from db.dbutils import *

logger = logging.getLogger(__name__)

from datetime import datetime, date


def dbsetup():
    try:
        cnx = getconn()
        create_database(cnx)
        print("Database created")
    except:
        print("Error in creating DB")
        exit(1)


def getdbs():
    mydb = getconn()
    mycursor = mydb.cursor()

    mycursor.execute("SHOW DATABASES;")
    dbs = mycursor.fetchall()
    dbs = [x[0] for x in dbs]
    mydb.close()
    return dbs


def get_emp_list():
    mydb = getconn()
    dbs = get_data(mydb)
    emplist = []
    for v in dbs:
        empdata = {}
        empdata['empid'] = v[0]
        empdata['fname'] = v[1]
        empdata['lname'] = v[2]
        empdata['hdate'] = datetime.strftime(v[3], "%d-%m-%Y")
        emplist.append(empdata)
    mydb.close()
    return emplist


def insert_emp(mem_info):
    mydb = getconn()
    if not mem_info:
        data = ('Uday', 'Sankar', datetime.now().date(), 'M', date(1989, 3, 10))
    else:
        data = (
            mem_info['fname'], mem_info['lname'], datetime.strptime(mem_info['doj'], "%d-%m-%Y").date(), mem_info['gender'],
        datetime.strptime(mem_info['dob'], "%d-%m-%Y").date())
        # first_name, last_name, hire_date, gender, birth_date

    logger.info("Emp added:", insertemp(mydb, data))
    mydb.close()
    return
