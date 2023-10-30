import sqlite3
from pathlib import Path


massge = """"
a __> = add Task
d __> = deleat Task
s __> = shaow all Tasks
u __> = updat Task
q __> = quit App
pleas chosse 
"""
while massge != "q":


    user = input(massge).strip().lower()

            
    commend = ["a" , "d", "s", "u", "q"]



    user_id2 = 1
    try:
        sql = sqlite3.connect(Path.home() / Path("Desktop" , "task.db"))
        crsr = sql.cursor()

    except:
        print("no concet")

    finally:
        if (sql):
            ail2 =''' CREATE TABLE if not exists tasks (
            user_id INTGER,
            name_task VARCHER(20),
            decription TEXT
            )
            '''
            crsr.execute(ail2)
            
            def add_task():
                task_name = input("inter name task:").strip()
                des = input("intar decription:").strip()

                crsr.execute(f" INSERT INTO tasks (user_id ,name_task, decription ) VALUES('{user_id2}','{task_name}','{des}')")

                sql.commit()
                


            def deleat_task():
                task_name = input("writ the name task :")
                crsr.execute(f"DELETE FROM tasks WHERE name_task= '{task_name}' and user_id = '{user_id2}' ")
                sql.commit()
                


            def shaow_task():
                crsr.execute(f"SELECT * FROM tasks where user_id= '{user_id2}'")
                resalt =crsr.fetchall()
                
                if len(resalt)> 0:
                    for i in resalt:
                        print(f"task name is{i[1]} and", end=" ")
                        print(f"Descrtion is {i[2]}")
                        


            def updat_task():
                task_name =input(" enter the task name to updat:").strip()
                crsr.execute(f"SELECT * FROM tasks WHERE name_task = '{task_name}'AND user_id = '{user_id2}' ")
                re = crsr.fetchall()
                if not re :
                    print("is not find the tasks   ")



                else:
                    des = input(" inter the descrption:")
                    crsr.execute(f"UPDATE tasks SET decription = '{des}' WHERE name_task = '{task_name}' AND user_id = '{user_id2}'  ")
                    sql.commit()    

            def quit_task():
                print("the programing is close")
                exit()


            

            if user in commend:
                if user == "a":
                    add_task()


                elif user == "d":
                    deleat_task()



                elif user == "s":
                    shaow_task()    




                elif user == "u":
                    updat_task()





                elif user == "q":
                    quit_task()


            else:
                print("the commend not true")

        sql.close()        