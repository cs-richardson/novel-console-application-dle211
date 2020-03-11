import sqlite3 as sq
from datetime import datetime, date

con = sq.connect("/Users/tuandunglephan/Desktop/IB CS/sql/novel.db")
c = con.cursor()

def getAuthors():
    c.execute("SELECT * FROM Authors")
    data = c.fetchall()
    return data

def getConsumers():
    c.execute("SELECT * FROM Consumers")
    data = c.fetchall()
    return data

def getNovels():
    c.execute("SELECT * FROM Novels")
    data = c.fetchall()
    return data

def getPurchases():
    c.execute("SELECT * FROM Purchases")
    data = c.fetchall()
    return data

def registerAuthor(name, date):
    authors = getAuthors()
    ins_str = 'INSERT INTO Authors VALUES (' + str(authors[-1][0] + 1) + ', "' + str(name) + '", "' + str(date) + '");'
    c.execute(ins_str)
    con.commit()

def registerConsumer(name, date):
    consumers = getConsumers()
    ins_str = 'INSERT INTO Consumers VALUES (' + str(consumers[-1][0] + 1) + ', "' + str(name) + '", "' + str(date) + '");'
    c.execute(ins_str)
    con.commit()

def registerNovel(authorID, name, date):
    novels = getNovels()
    ins_str = 'INSERT INTO Novels VALUES (' + str(novels[-1][0] + 1) + ', ' + str(authorID) + ', "' + str(name) + '", "' + str(date) + '");'
    c.execute(ins_str)
    con.commit()

def logPurchase(consumerID, novelID, date, quantity):
    ins_str = 'INSERT INTO Purchases VALUES (' + str(consumerID) + ', ' + str(novelID) + ', "' + str(date) + '", ' + str(quantity) + ');'
    c.execute(ins_str)
    con.commit()


def endProgram():
    con.close()


def renderMainMenu():
    choice = -1

    while choice != 0:
        print("\nMain Menu")
        print("–––––––––")
        print("1. Register")
        print("2. Purchase")
        print("3. Admin")
        print("0. Exit")
        choice = int(input("Choose an option: "))

        try:
            if choice == 1:
                renderRegistrationMenu()
            elif choice == 2:
                renderPurchaseRequest()
            elif choice == 3:
                renderAdminRequest()
            elif choice == 0:
                print("Exiting program...")
            else:
                print("Invalid option.")
        except ValueError:
            print("Invalid option.")

    endProgram()


def renderRegistrationMenu():
    choice = -1

    while choice != 0:
        print("\nMain Menu > Register")
        print("––––––––––––––––––––")
        print("1. As an Author")
        print("2. As a Consumer")
        print("3. As a Novel")
        print("0. Back")
        
        choice = int(input("Choose an option: "))
        try:
            if choice == 1:
                renderAuthorRegistration()
                choice = 0
            elif choice == 2:
                renderConsumerRegistration()
                choice = 0
            elif choice == 3:
                renderNovelRegistration()
                choice = 0
            elif choice == 0:
                pass
            else:
                print("Invalid option.")
        except ValueError:
            print("Invalid option.")


def renderAuthorRegistration():
    print("\nMain Menu > Register > Author > Date Of Birth")
    print("–––––––––––––––––––––––––––––––––––––––––––––")
    day = int(input("Enter day: "))
    month = int(input("Enter month: "))
    year = int(input("Enter year: "))

    print("\nMain Menu > Register > Author > Name")
    print("––––––––––––––––––––––––––––––––––––")
    name = str(input("Enter name: "))

    checkAndEnterAuthorSelection(day, month, year, name)


def renderConsumerRegistration():
    print("\nMain Menu > Register > Consumer > Date Of Birth")
    print("–––––––––––––––––––––––––––––––––––––––––––––––")
    day = int(input("Enter day: "))
    month = int(input("Enter month: "))
    year = int(input("Enter year: "))

    print("\nName")
    name = str(input("Enter name: "))

    checkAndEnterConsumerSelection(day, month, year, name)


def renderNovelRegistration():
    print("\nMain Menu > Register > Novel")
    print("––––––––––––––––––––––––––––")
    print("Date Of Publication")
    day = int(input("Enter day: "))
    month = int(input("Enter month: "))
    year = int(input("Enter year: "))

    print("\nAuthor")
    renderAuthorTable()
    author = str(input("Enter the author ID: "))

    print("\nName")
    name = str(input("Enter name: "))

    checkAndEnterNovelSelection(day, month, year, author, name)


def renderPurchaseRequest():
    print("\nMain Menu > Purchase")
    print("––––––––––––––––––––")
    print("Date Of Purchase")
    day = int(input("Enter day: "))
    month = int(input("Enter month: "))
    year = int(input("Enter year: "))

    consumerSelection = consumer_lb()
    novelSelection = novel_lb()
    quantityInput = quantity_lb()

    checkAndEnterPurchaseSelection(day, month, year, consumerSelection, novelSelection, quantityInput)


def renderAdminRequest():
    userInput = "a"
    password = "1234"
    
    while userInput != "0":
        print("\nMain Menu > Admin")
        print("–––––––––––––––––")
        print("0. Back")
        userInput = str(input("Enter password: "))

        if userInput == password:
            print("Logging in...")
            renderAdminMenu()
            userInput = "0"
        elif userInput == "0":
            pass
        else:
            print("Wrong password.")


def renderAdminMenu():
    choice = -1

    while choice != 0:
        print("\nMain Menu > Admin")
        print("–––––––––––––––––")
        print("1. Author Report")
        print("2. Consumer Report")
        print("3. Novel Report")
        print("4. Purchase Report")
        print("0. Log Out")
        choice = int(input("Choose an option: "))

        try:
            if choice == 1:
                print("\nMain Menu > Admin > Author Report")
                renderAuthorTable()
            elif choice == 2:
                print("\nMain Menu > Admin > Consumer Report")
                renderConsumerTable()
            elif choice == 3:
                print("\nMain Menu > Admin > Novel Report")
                renderNovelTable()
            elif choice == 4:
                print("\nMain Menu > Admin > Purchase Report")
                renderPurchaseTable()
            elif choice == 0:
                print("Logging out...")
            else:
                print("Invalid option.")
        except ValueError:
            print("Invalid option.")


def renderAuthorTable():
    authors = getAuthors()

    print("–––––––––––––––––––––––––––––––––––––––––––")

    print("AuthorID\tAuthorName\tDateOfBirth")
    print("–––––––––––––––––––––––––––––––––––––––––––")

    for r in range(len(authors)):
        for c in range(len(authors[r])):
            if len(str(authors[r][c])) <= 7:
                print(authors[r][c], end="\t\t")
            elif len(str(authors[r][c])) > 7:
                print(authors[r][c], end="\t")

        print("\n–––––––––––––––––––––––––––––––––––––––––––")


def renderConsumerTable():
    consumers = getConsumers()

    print("–––––––––––––––––––––––––––––––––––––––––––")

    print("ConsumerID\tConsumerName\tDateOfBirth")
    print("–––––––––––––––––––––––––––––––––––––––––––")

    for r in range(len(consumers)):
        for c in range(len(consumers[r])):
            if len(str(consumers[r][c])) <= 7:
                print(consumers[r][c], end="\t\t")
            elif len(str(consumers[r][c])) > 7:
                print(consumers[r][c], end="\t")

        print("\n–––––––––––––––––––––––––––––––––––––––––––")


def renderNovelTable():
    novels = getNovels()

    print("–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––")

    print("NovelID\t\tAuthorID\tNovelName\tDateOfPublication")
    print("–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––")

    for r in range(len(novels)):
        for c in range(len(novels[r])):
            if len(str(novels[r][c])) <= 7:
                print(novels[r][c], end="\t\t")
            elif len(str(novels[r][c])) > 7:
                print(novels[r][c], end="\t")

        print("\n–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––")


def renderPurchaseTable():
    purchases = getPurchases()

    print("––––––––––––––––––––––––––––––––––––––––––––––––––––––––")

    print("ConsumerID\tNovelID\t\tDateOfPurchase\tQuantity")
    print("––––––––––––––––––––––––––––––––––––––––––––––––––––––––")

    for r in range(len(purchases)):
        for c in range(len(purchases[r])):
            if len(str(purchases[r][c])) <= 7:
                print(purchases[r][c], end="\t\t")
            elif len(str(purchases[r][c])) > 7:
                print(purchases[r][c], end="\t")

        print("\n––––––––––––––––––––––––––––––––––––––––––––––––––––––––")


def consumer_lb():
    print("\nMain Menu > Purchase > Consumer")
    renderConsumerTable()
    
    consumer = int(input("Enter the consumer ID: "))
    return consumer


def novel_lb():
    print("\nMain Menu > Purchase > Novel")
    renderNovelTable()
    
    novel = int(input("Enter the novel ID: "))
    return novel


def quantity_lb():
    print("\nMain Menu > Purchase > Quantity")
    print("–––––––––––––––––––––––––––––––")

    quantity = int(input("Enter quantity: "))
    return quantity


def checkAndEnterAuthorSelection(d, m, y, n):
    print("Registering author...")
    try:
        dt = date(int(y), int(m), int(d))
        registerAuthor(n, dt)
        print("\nSuccess")
        print("–––––––")
        print("You have registered an author.")
    except:
        print("\nError")
        print("–––––")
        print("Possible reasons:\n- You chose an invalid date.")
        return


def checkAndEnterConsumerSelection(d, m, y, n):
    print("Registering consumer...")
    try:
        dt = date(int(y), int(m), int(d))
        registerConsumer(n, dt)
        print("\nSuccess")
        print("–––––––")
        print("You have registered a consumer.")
    except:
        print("\nError")
        print("–––––")
        print("Possible reasons:\n- You chose an invalid date.")
        return


def checkAndEnterNovelSelection(d, m, y, a, n):
    print("Registering novel...")
    try:
        dt = date(int(y), int(m), int(d))
        registerNovel(a, n, dt)
        print("\nSuccess")
        print("–––––––")
        print("You have registered a novel.")
    except:
        print("\nError")
        print("–––––")
        print("Possible reasons:\n- You chose an invalid author and/or date.")
        return


def checkAndEnterPurchaseSelection(d, m, y, c, n, q):
    print("Logging purchase...")
    try:
        dt = date(int(y), int(m), int(d))
        logPurchase(c, n, dt, q)
        print("\nSuccess")
        print("–––––––")
        print("You have purchased books.")
    except:
        print("\nError")
        print("–––––")
        print("Possible reasons:\n- There is already a purchase for that combination.\n- You chose an invalid consumer, novel and/or date.")
        return


print("\nWelcome to Amazone's online shop!")
input("Press ENTER to continue.")
renderMainMenu()