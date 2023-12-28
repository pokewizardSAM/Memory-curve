import mysql.connector as mysql
import time
import os
import subprocess
from tabulate import tabulate
import special_functions as spf

conn_obj = mysql.connect(host="localhost",
                         user="root",
                         password="3561"
                         )

cur = conn_obj.cursor()
cur.execute(r"CREATE DATABASE IF NOT EXISTS MEM_RECURVE;")
cur.execute(r"USE MEM_RECURVE;")

def date():
    cur.execute("USE MEM_RECURVE;")
    cur.execute("SELECT CURDATE()")
    date = cur.fetchone()
    print(f"Date: {date[0]}")

def show_all_db():
    spf.refresh_screen()
    date()
    cur.execute("SHOW DATABASES;")
    return spf.centre_table(cur.fetchall(),"grid")

def get_subjects(table):
    cur .execute("SELECT SUBJECT FROM {}".format(table))
    subject = cur.fetchall()
    return subject

def upadte_recurve_db():
    # CREATE TABLE IF NOT EXISTS 
    cur = conn_obj.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS RECURVE_TABLE01 (
            CHAPTER_ID INT AUTO_INCREMENT PRIMARY KEY,
            SUBJECT VARCHAR(10) NOT NULL,
            CHAPTER_NAME VARCHAR(50) NOT NULL,
            LAST_STUDY_DATE DATE NOT NULL,
            STREAK INT NOT NULL,
            STUDY_SCORE INT NOT NULL
        );
        """)
    
    all_subject = get_subjects("RECURVE_TABLE01")
    # print(f"{type(subject)}, {subject}") # debugging flair
    if all_subject == []:
        spf.centre_table([["-------!!!!!!!!!!!!  THERE ARE NO SUBJECTS IN THE RECORD  !!!!!!!!!!!!----"]],"fancy_grid")
        spf.centre_table([["-------SELECT FROM THE DEFAULT SUBJECTS-------"],["PHYSICS"], ["CHEMISTRY"],["MATHS"]],"fancy_grid")
        
        # cur.execute("""INSERT INTO RECURVE_TABLE01 (SUBJECT) VALUES ("PHYSICS"),("MATHS"),("CHEMISTRY");""")
    else:    
        spf.centre_table([all_subject], "grid")

    current_subject = input("\nPlease Select which subject you want to Update: ").upper()
    cur.execute("SELECT CHAPTER_NAME FROM RECURVE_TABLE01 WHERE SUBJECT = '{}';".format(current_subject))
    current_chapters = cur.fetchall()
    if current_chapters == []:
        spf.centre_table([["-------!!!!!!!!!!!!  YOU HAVEN'T CREATED ANY CHAPTERS  !!!!!!!!!!!!----"]],"fancy_grid")
        chap_name = input("** Creating a new chapter....... \n** Name for new chapter: ")

        spf.centre_txt(f"Selected Chap ->> {chap_name} ", artifacts=False)
    else:
        spf.centre_table([current_chapters],'fancy_grid')
        print("Select chapter : ", end="")
        spf.centre_txt(f"Selected Chap ->> {chap_name} ", artifacts=False)
    
    
    
    time.sleep(2)
    return 


# def 
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
        elif usr_choice == 4:
            exit()
            

        


main()