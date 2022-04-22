from datetime import datetime, date

import faker

from HW_11.src import app
from flask import render_template, request, redirect
from HW_11.src.models import Note, Tag, db_session, Contact

fake_data = faker.Faker('ru-RU')


@app.route('/', strict_slashes=False)
def index():
    q = request.args.get('q')
    find_contact = request.args.get('find_contact')
    if find_contact:
        contacts = [db_session.query(Contact).filter(Contact.name == find_contact).first()]
    else:
        contacts = db_session.query(Contact).all()
    if q:
        notes = [db_session.query(Note).filter(Note.name == q).first()]
    else:
        notes = db_session.query(Note).all()
    return render_template('pages/index.html', notes=notes, contacts=contacts)


@app.route("/delete/note/<id>", strict_slashes=False)
def delete_note(id):
    db_session.query(Note).filter(Note.id == id).delete()
    db_session.commit()

    return redirect("/")


@app.route("/delete/contact/<id>", strict_slashes=False)
def delete_contact(id):
    db_session.query(Contact).filter(Contact.id == id).delete()
    db_session.commit()

    return redirect("/")


@app.route("/done/<id>", strict_slashes=False)
def done(id):
    db_session.query(Note).filter(Note.id == id).first().done = True
    db_session.commit()

    return redirect("/")


@app.route("/note/", methods=["GET", "POST"], strict_slashes=False)
def add_note():
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        tags = request.form.getlist("tags")
        tags_obj = []
        for tag in tags:
            tags_obj.append(db_session.query(Tag).filter(Tag.name == tag).first())
        note = Note(name=name, description=description, tags=tags_obj)
        db_session.add(note)
        db_session.commit()
        return redirect("/")
    else:
        tags = db_session.query(Tag).all()

    return render_template("pages/note.html", tags=tags)


@app.route("/tag/", methods=["GET", "POST"], strict_slashes=False)
def add_tag():
    if request.method == "POST":
        name = request.form.get("name")
        tag = Tag(name=name)
        db_session.add(tag)
        db_session.commit()
        return redirect("/note/")

    return render_template("pages/tag.html")


@app.route("/contact/", methods=["GET", "POST"], strict_slashes=False)
def add_contact():
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        birthday = request.form.get("birthday")
        email = request.form.get("email")
        address = request.form.get("address")
        datetime_obj = datetime.fromisoformat(birthday)
        
        contact = Contact(name=name, phone=phone, birthday=datetime_obj, email=email, address=address)
        db_session.add(contact)
        db_session.commit()
        return redirect("/")

    return render_template("pages/contact.html")


@app.route('/edit/<id>', methods=['GET', 'POST'], strict_slashes=False)
def contact_edit(id):
    contact = db_session.query(Contact).filter(Contact.id == id).first()
    if request.method == 'POST':
        name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        address = request.form.get("address")
        contact.name = name
        contact.phone = phone
        contact.email = email
        contact.address = address
        db_session.commit()
        return redirect('/')
    return render_template('pages/edit.html', title='Upload Service', contact=contact)


@app.route('/edit_note/<id>', methods=['GET', 'POST'], strict_slashes=False)
def note_edit(id):
    note = db_session.query(Note).filter(Note.id == id).first()
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        tags = request.form.getlist("tags")
        tags_obj = []
        for tag in tags:
            tags_obj.append(db_session.query(Tag).filter(Tag.name == tag).first())
        note.name = name
        note.description = description
        note.tags = tags_obj
        db_session.commit()
        return redirect("/")
    else:
        tags = db_session.query(Tag).all()
    return render_template('pages/edit_note.html', title='Upload Service', tags=tags, note=note)
