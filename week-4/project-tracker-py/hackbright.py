"""Hackbright Project Tracker.

A front-end for a database that allows users to work with students, class
projects, and the grades students receive in class projects.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///hackbright'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


def get_student_by_github(github):
    """Given a GitHub account name, print info about the matching student."""

    QUERY = """
        SELECT first_name, last_name, github
        FROM students
        WHERE github = :github
        """

    db_cursor = db.session.execute(QUERY, {'github': github})

    row = db_cursor.fetchone()

    if row:
        print("Student: {} {}\nGitHub account: {}".format(row[0], row[1], row[2]))
    else:
        print("{} account does not exist".format(github))


def make_new_student(first_name, last_name, github):
    """Add a new student and print confirmation.

    Given a first name, last name, and GitHub account, add student to the
    database and print a confirmation message.
    """
    QUERY = """ INSERT INTO students (first_name, last_name, github)
    VALUES (:first_name, :last_name, :github)
    """
    db.session.execute(QUERY, {'first_name': first_name, 'last_name': last_name, 'github': github })

    db.session.commit()

    print("Student {} {} with GitHub account {} successfully added!".format(first_name, last_name, github))


def get_project_by_title(title):
    """Given a project title, print information about the project."""

    QUERY = """ SELECT title, description, max_grade
    FROM projects
    WHERE title = :title """

    db_cursor = db.session.execute(QUERY, {'title': title})

    row = db_cursor.fetchone()

    if row:
        print("Project: {}\nDescription: {}\nMax Grade: {}".format(row[0], row[1], row[2]))
    else:
        print("{} does not exist".format(title))


def get_grade_by_github_title(github, title):
    """Print grade student received for a project."""
    QUERY = """ SELECT grade
    FROM grades
    WHERE student_github = :github AND project_title = :title"""

    db_cursor = db.session.execute(QUERY, {'github': github, 'title': title})
    row = db_cursor.fetchone()

    if row:
        print("Student github: {}\nGrade: {}".format(github, row[0]))
    else:
        print("No grade exists for {} by {}".format(title, github))


def assign_grade(github, title, grade):
    """Assign a student a grade on an assignment and print a confirmation."""

    QUERY = """ INSERT INTO grades (student_github, grade, project_title)
    VALUES (:github, :grade, :title)"""

    db.session.execute(QUERY, {'github': github, 'grade': grade, 'title': title})

    db.session.commit()

    print("Student github: {}\nGrade: {}\nProject: {}\nSuccessfully added.".format(github, grade, title))


def add_project(title, description, max_grade):

    QUERY = """ INSERT INTO projects (title, description, max_grade)
    VALUES (:title, :description, :max_grade)
    """

    db.session.execute(QUERY, {'title': title, 'description': description, 'max_grade': max_grade})

    db.session.commit()

    print("Project {} with max grade {} was successfully added".format(title, max_grade))


def get_all_student_grades(student_github):
    QUERY = """ SELECT project_title, grade
    FROM grades
    WHERE student_github = :github"""

    db_cursor = db.session.execute(QUERY, {"github": student_github})
    all_results = db_cursor.fetchall()

    if all_results:
        for result in all_results:
            print("Project Title: {}, Grade: {}".format(result[0], result[1]))
    else:
        print("No grades exist in database for {}".format(student_github))


def handle_input():
    """Main loop.

    Repeatedly prompt for commands, performing them, until 'quit' is received as a
    command."""

    command = None

    while command != "quit":
        input_string = input("HBA Database> ")
        tokens = input_string.split()
        if tokens != ["quit"] and len(tokens) < 2:
            print("Please enter a command and at least one argument.")
        else:
            command = tokens[0]
            args = tokens[1:]

            if command == "student":
                github = args[0]
                get_student_by_github(github)

            elif command == "new_student":
                if len(args) == 3:
                    first_name, last_name, github = args  # unpack!
                    make_new_student(first_name, last_name, github)
                else:
                    print("Please enter three arguments.")

            elif command == "project_title":
                title = args[0]
                get_project_by_title(title)

            elif command == "get_grade":
                if len(args) == 2:
                    github, title = args
                    get_grade_by_github_title(github, title)
                else:
                    print("Please enter two arguments.")

            elif command == "assign_grade":
                if len(args) == 3:
                    github, title, grade = args
                    if grade.isdigit():
                        assign_grade(github, title, grade)
                    else:
                        print("Grade must be a number.")
                else:
                    print("Please enter three arguments.")

            elif command == "add_project":
                if len(args) >= 3:
                    title = args[0]
                    description = " ".join(args[1:-1])
                    max_grade = args[-1]
                    if max_grade.isdigit():
                        add_project(title, description, max_grade)
                    else:
                        print("Max grade must be a number.")
                else:
                    print("Please enter three arguments.")

            elif command == "get_all_grades":
                github = args[0]
                get_all_student_grades(github)

            else:
                if command != "quit":
                    print("Invalid Entry. Try again.")


if __name__ == "__main__":
    connect_to_db(app)

    handle_input()

    # To be tidy, we close our database connection -- though,
    # since this is where our program ends, we'd quit anyway.

    db.session.close()
