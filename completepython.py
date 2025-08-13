import csv
import os
import matplotlib.pyplot as plt

FILENAME = "off_study_log"

def add_entry():
    subject = input("What subject are you studying?").strip()
    try:
        hours = float(input("How many hours?").strip())
    except ValueError:
        print("please enter a number for hours.")
        return

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([subject, hours])

    print(f"added {hours} hours for {subject}.\n")



def show_chart():
    totals = get_totals()
    if not totals:
        return

    subjects = list(totals.keys())
    hours = list(totals.values())

    plt.bar(subjects, hours, color='skyblue')
    plt.xlabel("Subjects")
    plt.ylabel("Total Hours")
    plt.title("Study Hours by Subject")
    plt.show()



def view_totals():
    if not os.path.exists(FILENAME):
        print("no data yet!\n")
        return
    totals = {}
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) < 2:
                continue       #skips incomplete rows
            try:
                subject = row[0].strip()
                hours = float(row[1].strip())
            except ValueError:  
                continue      #skips rows the hours cant be changed into string
            totals[subject] = totals.get(subject, 0) + hours

    print("\n Total study hours so far:")
    for subject, total_hours in totals.items():
        print(f"{subject}: {total_hours} hours")
    print()


def view_all_entries():
    if not os.path.exists(FILENAME):
        print("no data yet!\n")
        return
    print("\n All study entries:")
    totals = {}
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2:
                print(f"subject: {row[0]}, Hours: {row[1]}")
    print()



while True:
    print("What would you like to do?")
    print("1 - Add a study entry")
    print("2 - View total hours per subject")
    print("3 - view all entries")
    print("4 - view charts of study hours")
    print("5 - Quit")

    choice = input("choice: ").strip()

    if choice == "1":
        add_entry()
    elif choice == "2":
        view_totals()
    elif choice == "3":
        view_all_entries()
    elif choice == "4":
        show_charts()
    elif choice == "5":
        print("Goodbye! ")
        break
    else:
        print("Invalid choice, please try again.\n")



















        
