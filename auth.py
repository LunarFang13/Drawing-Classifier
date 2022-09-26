import mysql.connector

def connectdb():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database = "drawing-classifier"
    )
    cursor = mydb.cursor()
    return([mydb, cursor])

def endconn(db):
    db.close()

def register(username, passwd):
    conn = connectdb()
    c = conn[1]
    db = conn[0]
    try:
        c.execute(f"insert into authentication(username, password) values ('{username}', '{passwd}');")
        db.commit()
        print("User successfully added")
    except mysql.connector.errors.IntegrityError as e:
        print("Username already exists")
    endconn(db)


def login(username, passwd):
    conn = connectdb()
    c = conn[1]
    db = conn[0]
    c.execute(f"Select pid, password from authentication where username = '{username}'")
    res = c.fetchall()
    print(res)
    if (len(res)==0):
        print("Invalid username")
        endconn(db)
        return False
    pid = res[0][0]
    dbpass = res[0][1]
    if(dbpass == passwd):
        endconn(db)
        print(f"logged in as user id : {pid}")
        return True

    endconn(db)
    print("Invalid password")
    return False

