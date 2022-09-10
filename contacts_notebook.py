import sqlite3


db = sqlite3.connect("app.db")


cr = db.cursor()

cr.execute("create table if not exists contacts (name text, number integer)")


def commit_and_close():
    """Commit Changes and Close Connection To Database"""
    db.commit()
    db.close()
    print("Connection To Database Is Closed")


commands_list = ["s", "a", "d", "u", "q"]


def show_contacts():

    cr.execute(f"select * from contacts")

    results = cr.fetchall()

    print(f"You Have {len(results)} contacts.")

    if len(results) > 0:

        print("Showing all contacts: ")

    for row in results:

        print(f"contact => {row[0]},", end=" ")

    question = input("wanna do anything else? ")

    if question == "yes":
        start()

    else:
        commit_and_close()


def add_contact():

    co = input("Write contact Name: ").strip().capitalize()

    cr.execute(
        f"select name from contacts where name = '{co}'")

    results = cr.fetchone()

    if results == None:

        numb = input("Write the contact'S number ").strip()

        cr.execute(
            f"insert into contacts(name, number) values('{co}', '{numb}')")

    else:

        print("it already exists")

    question = input("wanna do anything else? ")

    if question == "yes":
        start()
    else:
        commit_and_close()


def delete_contact():

    co = input("Write the contact's name: ").strip().capitalize()

    cr.execute(f"delete from contacts where name = '{co}'")

    question = input("wanna do anything else? ")

    if question == "yes":
        start()
    else:
        commit_and_close()


def update_contact():

    co = input("Write contact's name: ").strip().capitalize()

    numb = input("Write The New contact's number ").strip()

    cr.execute(
        f"update contacts set number = '{numb}' where name = '{co}'")

    question = input("wanna do anything else? ")

    if question == "yes":
        start()
    else:
        commit_and_close()


def start():
    input_message = """
    What Do You Want To Do ?
    "s" => Show All contacts
    "a" => Add New contact
    "d" => Delete A contact
    "u" => Update a contact
    "q" => Quit The App
    Choose Option:
    """
    global user_input
    user_input = input(input_message).strip().lower()

    if user_input in commands_list:
        if user_input == "s":
            show_contacts()
        elif user_input == "a":
            add_contact()
        elif user_input == "d":
            delete_contact()
        elif user_input == "u":
            update_contact()
        else:
            print("App Is Closed.")
            commit_and_close()
    else:
        print(f"Sorry This Command \"{user_input}\" Is Not Found")


start()
