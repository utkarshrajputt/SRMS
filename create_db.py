import sqlite3
def create_db():
    con=sqlite3.connect(database="srms.db")
    cur=con.cursor()
    
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text,duration text,charges INTEGER,description text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,dob text,contact text,admission text,course text,state text,city text,pin text,address text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT,roll INTEGER,name text,course text,marks_ob INTEGER,full_marks INTEGER,per REAL)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,f_name text,l_name text,contact text,email text,question text,answer text,password text)")
    con.commit()

    con.close()
    
    # https://sqliteviewer.app/
create_db()