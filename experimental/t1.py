import sqlite3
con = sqlite3.connect("huesillo.db")
cur = con.cursor()
cur.execute("DROP TABLE maestro")
cur.execute("CREATE TABLE maestro(master_id INTEGER PRIMARY KEY, username TEXT, pass TEXT, email TEXT UNIQUE)")
#cur.execute("CREATE TABLE stock(stock_id INTEGER PRIMARY KEY, master_id INTEGER, current_stock INTEGER, FOREIGN KEY(master_id) REFERENCES maestro (master_id))")
#cur.execute("CREATE TABLE ventas(ventas_id INTEGER PRIMARY KEY, master_id INTEGER, current_ventas INTEGER, FOREIGN KEY(master_id) REFERENCES maestro (master_id))")
#res = cur.execute("SELECT name FROM sqlite_master")
#print(res.fetchone())