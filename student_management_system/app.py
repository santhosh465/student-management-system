from flask import Flask, render_template, request, redirect
from database import (
    create_database,
    add_student,
    get_all_students,
    get_student,
    update_student,
    delete_student
)

app = Flask(__name__)

# ✅ THIS LINE FIXES EVERYTHING
create_database()


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

        add_student(name, email, course, int(year))
        return redirect("/")

    return render_template("add.html")


@app.route("/edit/<int:student_id>", methods=["GET", "POST"])
def edit(student_id):
    student = get_student(student_id)

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
    app.run(host="0.0.0.0", port=5000) 
