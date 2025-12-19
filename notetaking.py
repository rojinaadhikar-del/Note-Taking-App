def add_note():
    note = input("Enter your note:")
    with open("note.txt", "a") as file:
        file.write(note + "\n")
    print("Note id added!")


def view_note():
    try:
        with open("note.txt", "r")as file:
            notes = file.readlines()

        if not notes:
            print("No notes found.")
        else:
            print("\nYour Notes:")
            count = 1
            for note in notes:
                print(note.strip())
                count = +=1
     except FileNotFoundError:
        print("No notes found.")

def clear_notes():
    open("note,txt", "w"). close()
    print("All notes cleared!")

while True:
    print("\nNote.taking App")
    print("1. Add a note")
    print("2. View all notes")
    print("3. Clear all notes")
    print("4. Exit")

    choice =input("Choose a feature(1-4):")


    if choice == "1":
        add_note()
    elif choice =="2":
        view_notes()
    elif choice == "3":
        clear_notes()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Please choose from the given option")    

             