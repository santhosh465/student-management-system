from flask import Flask, render_template, request, redirect
from database import (
    create_database,
    get_all_students,
    add_student,
    update_student,
    delete_student,
    get_student_by_id
)

app = Flask(__name__)

@app.route("/")
def home():
    students = get_all_students()
    return render_template("index.html", students=students)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        course = request.form["course"]
        year = request.form["year"]

        if name and email and course and year:
            add_student(name, email, course, int(year))

        return redirect("/")

    return render_template("add.html")

@app.route("/edit/<int:student_id>", methods=["GET", "POST"])
def edit(student_id):
    student = get_student_by_id(student_id)

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        course = request.form["course"]
        year = request.form["year"]

        update_student(student_id, name, email, course, int(year))
        return redirect("/")

    return render_template("edit.html", student=student)

@app.route("/delete/<int:student_id>")
def delete(student_id):
    delete_student(student_id)
    return redirect("/")

if __name__ == "__main__":
    create_database()
    app.run(host="0.0.0.0", port=5000) 

