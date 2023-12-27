import mysql.connector as mysql
import time
import os
import subprocess
from tabulate import tabulate
import special_functions as spf

conn_obj = mysql.connect(host="localhost",
                         user="root",
                         password="Alibha98"
                         )

cur = conn_obj.cursor()
cur.execute(r"CREATE DATABASE IF NOT EXISTS MEM_RECURVE;")
cur.execute(r"USE MEM_RECURVE;")

def date():
    cur.execute("SELECT CURDATE()")
    date = cur.fetchone()
    print(f"Date: {date[0]}")

def show_all_db():
    spf.refresh_screen()
    date()
    cur.execute("SHOW DATABASES;")
    return spf.centre_table(cur.fetchall(),"grid")

def upadte_recurve_db():
    cur = conn_obj.cursor()
    cur.execute("""
        USE MEM_RECURVE;
        CREATE TABLE IF NOT EXISTS RECURVE_TABLE01 (
            CHAPTER_ID INT NOT NULL PRIMARY KEY UNIQUE,
            SUBJECT VARCHAR(10) NOT NULL,
            CHAPTER_NAME VARCHAR(50) NOT NULL,
            LAST_STUDY_DATE DATE NOT NULL,
            STREAK INT NOT NULL,
            STUDY_SCORE INT NOT NULL
        );
        """)
    x = cur.fetchall()
    print(f"Db updated.")
    time.sleep(2)
    return 
def main_menu():
    spf.refresh_screen()
    date()
    spf.centre_table([["COMMANDS"]],"fancy_grid")
    spf.centre_table(spf.fix_list_for_tabulate(['UPDATE RECORD', "PLOT MEM RECORDS", "SAVE MEM RECORDS", "TIXE" ]) ,"fancy_grid")



def main():
    while True:
        main_menu()
        usr_choice = int(input("please enter your choice(1/2/3/4): "))
        if usr_choice == 1:
            upadte_recurve_db()
            

        


main()