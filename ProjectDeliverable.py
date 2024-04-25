import psycopg2

dbi = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="!J03tH35rO**",
    host="localhost",
    port=5432
)
db = dbi.cursor()


def interface():
    print("\nWelcome to the Database CLI Interface!\n")
    print("\nPlease select an option:\n")
    print("1. Insert Data\n")
    print("2. Delete Data\n")
    print("3. Update Data\n")
    print("4. Search Data\n")
    print("5. Aggregate Functions\n")
    print("6. Sorting\n")
    print("7. Joins\n")
    print("8. Groupings\n")
    print("9. Subqueries\n")
    print("10. Transactions\n")
    print("11. Error Handling\n")
    print("12. Exit\n")
    choice = input("\nEnter your choice (1-12): ")

    if choice == "1":
        insert()
        interface()
    elif choice == "2":
        delete()
        interface()
    elif choice == "3":
        update()
        interface()
    elif choice == "4":
        search()
        interface()
    elif choice == "5":
        aggregate()
        interface()
    elif choice == "6":
        sort()
        interface()
    elif choice == "7":
        join()
        interface()
    elif choice == "8":
        group()
        interface()
    elif choice == "9":
        subquery()
        interface()
    elif choice == "10":
        transaction()
        interface()
    elif choice == "11":
        handle()
        interface()
    elif choice == "12":
        exit()
    else:
        print("\n\n Please choose a valid number!!\n\n")
        interface()


def insert():
    choice1 = input("Enter 1 to insert into Player, 2 to insert into Game, and 3 to exit: ")
    if choice1 == "1":
        table = "Player"
    elif choice1 == "2":
        table = "Game"
    elif choice1 == "3":
        interface()
    else:
        insert()
    
    if choice1 == "1":
        columns = input("Enter a commaed list of the columns you would like to insert into: ")
        values = input("Enter a commaed list of the values you would like to insert: ")
        db_query = f"insert into Player ({columns}) values ({values});"
        db.execute(db_query)
    
    if choice1 == "2":
        columns = input("Enter a commaed list of the columns you would like to insert into: ")
        values = input("Enter a commaed list of the values you would like to insert: ")
        db_query = f"insert into Game ({columns}) values ({values});"
        db.execute(db_query)
    

def delete():
    choice1 = input("Enter 1 to delete from Player, 2 to delete from Game, and 3 to exit: ")
    if choice1 == "1":
        table = "Player"
    elif choice1 == "2":
        table = "Game"
    elif choice1 == "3":
        interface()
    else:
        delete()

    if choice1 == "1":
        condition = input("Enter the condition where you would like to delete data: ")
        db_query = f"delete from Player where {condition};"
        db.execute(db_query)

    if choice1 == "2":
        condition = input("Enter the condition where you would like to delete data: ")
        db_query = f"delete from Game where {condition};"
        db.execute(db_query)


def update():
    choice1 = input("Enter 1 to update Player, 2 to update Game, and 3 to exit: ")
    if choice1 == "1":
        table = "Player"
    elif choice1 == "2":
        table = "Game"
    elif choice1 == "3":
        interface()
    else:
        update()

    if choice1 == "1":
        column = input("Enter the column you would like to update: ")
        value = input("Enter the new value you would like to enter: ")
        condition = input("Enter the condition where you would like to update data: ")
        db_query = f"Update Player set {column} = {value} where {condition};"
        db.execute(db_query)
    
    if choice1 == "2":
        column = input("Enter the column you would like to update: ")
        value = input("Enter the new value you would like to enter: ")
        condition = input("Enter the condition where you would like to update data: ")
        db_query = f"Update Game set {column} = {value} where {condition};"
        db.execute(db_query)


def search():
    choice1 = input("Enter 1 to select from Player, 2 to select from Game, and 3 to exit: ")
    if choice1 == "1":
        table = "Player"
    elif choice1 == "2":
        table = "Game"
    elif choice1 == "3":
        interface()
    else:
        search()
    
    with_Condition = input("Input 1 if you would NOT like to include a condition and 2 if you would: ")
    if with_Condition == "1":
        if choice1 == "1":
            db.execute("Select * from Player;")
        if choice1 == "2":
            db.execute("Select * from Game;")
    elif with_Condition == "2":
        if choice1 == "1":
            condition = input("Enter the condition where you would like to search data: ")
            db_query = f"Select * from Player where {condition};"
            db.execute(db_query)
        if choice1 == "2":
            condition = input("Enter the condition where you would like to search data: ")
            db_query = f"Select * from Game where {condition};"
            db.execute(db_query)
    else:
        search()
    
    row_num = input("Enter the number of rows you would like to search (Enter 0 to fetch all):")
    if row_num == "0":
        rows = db.fetchall()
    elif row_num == "1":
        rows = db.fetchone()
    else:
        rows = db.fetchmany(size = int(row_num))

    for row in rows:
        print(row)
    print("\n")


def aggregate():
    choice1 = input("Enter 1 to aggregate Player, 2 to aggregate Game, and 3 to exit: ")
    if choice1 == "1":
        table = "Player"
    elif choice1 == "2":
        table = "Game"
    elif choice1 == "3":
        interface()
    else:
        aggregate()

    if choice1 == "1":
        funct = input("Enter the aggregate function you would like to use: ")
        column = input("Enter the column you would like to aggregate: ")
        db_query = f"Select {funct}({column}) from Player;"
        db.execute(db_query)
    if choice1 == "2":
        funct = input("Enter the aggregate function you would like to use: ")
        column = input("Enter the column you would like to aggregate: ")
        db_query = f"Select {funct}({column}) from Game;"
        db.execute(db_query)

    row = db.fetchone()
    print(row)
    print("\n")


def sort():
    choice1 = input("Enter 1 to sort Player, 2 to sort Game, and 3 to exit: ")
    if choice1 == "1":
        table = "Player"
    elif choice1 == "2":
        table = "Game"
    elif choice1 == "3":
        interface()
    else:
        sort()

    send = input("Enter if you want to sort the data ascending (1) or desending: ")
    if send == "1":
        if choice1 == "1":
            column = input("Enter the column you would like to sort: ")
            db_query = f"Select * from Player order by {column} asc;"
            db.execute(db_query)
        if choice1 == "2":
            column = input("Enter the column you would like to sort: ")
            db_query = f"Select * from Game order by {column} asc;"
            db.execute(db_query)
    else:
        if choice1 == "1":
            column = input("Enter the column you would like to sort: ")
            db_query = f"Select * from Player order by {column} desc;"
            db.execute(db_query)
        if choice1 == "2":
            column = input("Enter the column you would like to sort: ")
            db_query = f"Select * from Game order by {column} desc;"
            db.execute(db_query)
    
    row_num = input("Enter the number of rows you would like to search (Enter 0 to fetch all): ")
    if row_num == "0":
        rows = db.fetchall()
    elif row_num == "1":
        rows = db.fetchone()
    else:
        rows = db.fetchmany(size = int(row_num))

    for row in rows:
        print(row)
    print("\n")


def join():
    key1 = input("Enter the column from Player you would like to join: ")
    key2 = input("Enter the column from Game you would like to join: ")
    db_query = f"Select * from Player inner join Game on Player.{key1} = Game.{key2};"
    db.execute(db_query)

    row_num = input("Enter the number of rows you would like to search (Enter 0 to fetch all): ")
    if row_num == "0":
        rows = db.fetchall()
    elif row_num == "1":
        rows = db.fetchone()
    else:
        rows = db.fetchmany(size = int(row_num))

    for row in rows:
        print(row)
    print("\n")

def group():
    choice1 = input("Enter 1 to group Player, 2 to group Game, and 3 to exit: ")
    if choice1 == "1":
        table = "Player"
    elif choice1 == "2":
        table = "Game"
    elif choice1 == "3":
        print()
    else:
        group()

    if choice1 == "1":
        column = input("Enter the column you would like to group: ")
        db_query = f"Select {column}, count(*) from Player group by {column};"
        db.execute(db_query)
    if choice1 == "2":
        column = input("Enter the column you would like to group: ")
        db_query = f"Select {column}, count(*) from Game group by {column};"
        db.execute(db_query)
    
    row = db.fetchall()
    print(row)
    print("\n")


def subquery():
    outTable = input("Enter the table in the outer query: ")
    inTable = input("Enter the table in the inner query: ")
    outColumn = input("Enter the column in the outer query: ")
    inColumn = input("Enter the column in the inner query: ")
    db_query = f"Select * from {outTable} where {outColumn} in (select {inColumn} from {inTable});"
    db.execute(db_query)

    row_num = input("Enter the number of rows you would like to search (Enter 0 to fetch all): ")
    if row_num == "0":
        rows = db.fetchall()
    elif row_num == "1":
        rows = db.fetchone()
    else:
        rows = db.fetchmany(size = int(row_num))

    for row in rows:
        print(row)
    print("\n")


def transaction():
    db.execute("Begin transaction;")
    interface()
    dbi.commit()

def handle():
    
    try:
        interface()
    except Exception as e:
        print("Operation failed: ", e)

def exit():
    dbi.commit()
    db.close()
    dbi.close()

interface()