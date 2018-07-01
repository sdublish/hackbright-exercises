"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template, redirect, flash

import hackbright

app = Flask(__name__)
app.secret_key = "Whatever Comes Naturally"

@app.route("/")
def show_homepage():
    student_db = hackbright.db.session.execute("""SELECT github FROM students""")
    student_list = student_db.fetchall()

    project_db = hackbright.db.session.execute(""" SELECT title FROM projects """)
    project_list = project_db.fetchall()

    return render_template("homepage.html", students=student_list, projects=project_list)

@app.route("/student")
def get_student():
    """Show information about a student."""
    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)
    projects = hackbright.get_grades_by_github(github)

    return render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github,
                           projects=projects)


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""
    return render_template("student_search.html")


@app.route("/new-student")
def show_new_student_form():
    """ Show student add page """
    return render_template("new_student.html")


@app.route("/new-project")
def show_new_project_form():
    """ Show project add page """
    return render_template("new_project.html")


@app.route("/student-add", methods=["POST"])
def student_add():
    """ Adds student to database"""
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    github = request.form.get("github")

    hackbright.make_new_student(fname, lname, github)

    return render_template("added_student.html")


@app.route("/project-add", methods=["POST"])
def project_add():
    """ Adds project to the database """
    title = request.form.get("title")
    description = request.form.get("description")
    max_grade = request.form.get("max-grade")

    hackbright.add_project(title, description, max_grade)
    return render_template("added_project.html")


@app.route("/assign-grade")
def assign_grade():
    student_db = hackbright.db.session.execute("""SELECT github FROM students""")
    student_list = student_db.fetchall()

    project_db = hackbright.db.session.execute(""" SELECT title FROM projects """)
    project_list = project_db.fetchall()

    return render_template("assign_grade.html", students=student_list, projects=project_list)


@app.route("/grade-add", methods=["POST"])
def grade_add():
    """ Add grade """
    student = request.form.get("student")
    title = request.form.get("project")
    grade = request.form.get("grade")

    result = hackbright.get_grade_by_github_title(student, title)

    if result:
        hackbright.db.session.execute("""UPDATE grades
                                      SET grade={}
                                      WHERE student_github='{}'
                                      AND project_title='{}'""".format(grade, student, title))
        db.session.commit()
    else:
        hackbright.assign_grade(student, title, grade)

    flash("Grade successfully assigned.")
    return redirect("/")

@app.route("/project")
def list_projects():
    """ Lists all projects with info """
    project = request.args.get("title")

    title, description, max_grade = hackbright.get_project_by_title(project)
    completed_by_students = hackbright.get_grades_by_title(project)

    return render_template("project.html", title=title, description=description,
                           grade=max_grade, project_grades=completed_by_students)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
