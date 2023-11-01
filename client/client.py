from threading import Thread
import subprocess
from p_register import p_type
import sqlite3
import random
con = sqlite3.connect("huesillo.db")
cur = con.cursor()

t0 = Thread(target=subprocess.run, args=(["python3", "c_register_p.py"],))
t1 = Thread(target=subprocess.run, args=(["python3", "c_register.py"],))
t2 = Thread(target=subprocess.run, args=(["python3", "c_stock.py"],))
t3 = Thread(target=subprocess.run, args=(["python3", "c_sales.py"],))
t4 = Thread(target=subprocess.run, args=(["python3", "p_weekly.py"],))

t0.start()
t1.start()
t2.start()
t3.start()
t4.start()

while True:
    print("\nSelect an action:")
    print("1. Add a Master")
    print("2. Simulate")
    print("3. Stop producers")
    print("7. Clear database")
    print("8. ")
    print("9. exit")
    choice = input("Standing by... ")

    if choice == "1":
        type = bool(int(input("Paid subscription? 1 - y, 0 - n \n")))
        name = input("Enter name: \n")
        password = input("Enter your password: \n")
        email = input("Please enter your email: \n")
        message = name+","+password+","+email
        p_type(type, message)

    elif choice == "2":
        user0 = "aaa,aaa,aaa"
        user1 = "bbb,bbb,bbb"
        user2 = "ccc,ccc,ccc"
        user3 = "ddd,ddd,ddd"
        user4 = "eee,eee,eee"
        p_type(bool(random.getrandbits(1)), user0)
        p_type(bool(random.getrandbits(1)), user1)
        p_type(bool(random.getrandbits(1)), user2)
        p_type(bool(random.getrandbits(1)), user3)
        p_type(bool(random.getrandbits(1)), user4)
    elif choice == "3":
        continue
    elif choice == "7":
        cur.execute("DELETE FROM maestro")
        cur.execute("DELETE FROM ventas")
        cur.execute("DELETE FROM stock")
        con.commit()
    else:
        print("Option not admitted")