from tkinter import *

def start():
    students = []
    file = open("marks.txt", "r")
    lines = [ln.strip() for ln in file.readlines() if ln.strip()]
    file.close()
    for line in lines[1:]:
        parts = [p.strip() for p in line.split(",")]
        snumber = parts[0]
        name = parts[1]
        scores = list(map(int, parts[2:5]))
        total = int(parts[5])
        students.append({
            "number": snumber,
            "name": name,
            "scores": scores,
            "total": total
        })
        
    for s in students:
        cw = sum(s["scores"])
        pct = (s["total"] / 160) * 100
        if pct >= 70:
            s["grade"] = "A"
        elif pct >= 60:
            s["grade"] = "B"
        elif pct >= 50:
            s["grade"] = "C"
        elif pct >= 40:
            s["grade"] = "D"
        else:
            s["grade"] = "F"
    return students


def view_all():
    frame3text.delete(1.0, END)
    for s in students:
        frame3text.insert(END,
            f"Number: {s['number']}\n"
            f"Name: {s['name']}\n"
            f"Scores: {s['scores']}\n"
            f"Total: {s['total']}\n"
            f"Grade: {s['grade']}\n\n"
        )

def highest():
    frame3text.delete(1.0, END)
    highest = max(students, key=lambda x: x['total'])
    frame3text.insert(END,
        f"Highest:\n"
        f"Name: {highest['name']}\n"
        f"Number: {highest['number']}\n"
        f"Scores: {highest['scores']}\n"
        f"Total: {highest['total']}\n"
        f"Grade: {highest['grade']}\n"
    )

def lowest():
    frame3text.delete(1.0, END)
    lowest = min(students, key=lambda x: x['total'])
    frame3text.insert(END,
        f"Lowest:\n"
        f"Name: {lowest['name']}\n"
        f"Number: {lowest['number']}\n"
        f"Scores: {lowest['scores']}\n"
        f"Total: {lowest['total']}\n"
        f"Grade: {lowest['grade']}\n"
    )

def search():
    frame3text.delete(1.0, END)
    snumber = ent.get().strip()
    for s in students:
        if s['number'].strip() == snumber:
            frame3text.insert(END,
                f"{s['name']} (Number: {s['number']}):\n"
                f"Scores: {s['scores']}\n"
                f"Total: {s['total']}\n"
                f"Grade: {s['grade']}\n"
            )
    

root = Tk()
root.geometry('700x600')
root.title("Student Manager")

titel = Label(root, text='Student Manager', font=('Arial', 20, "bold"))
titel.pack(anchor="center", pady=20)

frame1 = Frame(root)
frame1.pack(padx=10, pady=10)

records = Button(frame1, text='View All Student Records', font=('Arial', 12), command=view_all)
records.pack(side="left", padx=10)

high = Button(frame1, text='Show Highest Score', font=('Arial', 12), command=highest)
high.pack(side="left", padx=10)

low = Button(frame1, text='Show Lowest Score', font=('Arial', 12), command=lowest)
low.pack(side="left", padx=10)

frame2 = Frame(root)
frame2.pack(anchor="center", pady=20)

titel1 = Label(frame2, text="View Individual Student Record(Student Number):", font=("Arial", 15))
titel1.pack(side="left", padx=10)

ent = Entry(frame2, font=("Arial", 12))
ent.pack(side="left", padx=10)

rec = Button(frame2, text='View Record', font=('Arial', 12), command=search)
rec.pack(side="left", padx=10)

frame3 = Frame(root, bg='white', bd=2, relief=SOLID)
frame3.pack(padx=20, pady=20, fill=BOTH, expand=True)

frame3text = Text(frame3, wrap=WORD, font=("Arial", 12), bd=0, borderwidth=0, relief=FLAT)
frame3text.pack(fill=BOTH, expand=True, padx=10, pady=10)

students = start()

root.mainloop()
