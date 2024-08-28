import os
import io
import csv
from modules.app import app
from flask import render_template, redirect, url_for, request, jsonify, flash, Response
from modules.models import db, Contact
from modules.read_vcf import read_vcf


@app.route('/', methods=['GET', 'POST'])
def index():
    search_query = request.args.get('search', '').strip()
    if search_query:
        contacts = Contact.query.filter(
            (Contact.phone.like(f'%{search_query}%')) |
            (Contact.name.like(f'%{search_query}%'))
        ).order_by(Contact.name).all()
    else:
        contacts = Contact.query.order_by(Contact.name).all()
    return render_template('index.html', contacts=contacts, search_query=search_query)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        phone = request.form.get('phone')
        name = request.form.get('name')

        while "  " in phone:
            phone = phone.replace("  ", " ")
        phone = phone.replace("  ", " ").strip()

        while "  " in name:
            name = name.replace("  ", " ")
        name = name.replace("  ", " ").strip()

        if Contact.query.filter_by(phone=phone).first():
            flash('Số điện thoại đã tồn tại!', 'error')
            return redirect(url_for('add'))

        if phone and name:
            new_contact = Contact(phone=phone, name=name)
            db.session.add(new_contact)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    contact = Contact.query.get_or_404(id)
    if request.method == 'POST':
        phone = request.form.get('phone')
        name = request.form.get('name')

        while "  " in phone:
            phone = phone.replace("  ", " ")
        phone = phone.replace("  ", " ").strip()

        while "  " in name:
            name = name.replace("  ", " ")
        name = name.replace("  ", " ").strip()

        if phone != contact.phone and Contact.query.filter_by(phone=phone).first():
            flash('Số điện thoại đã tồn tại!', 'error')
            return redirect(url_for('edit', id=id))

        contact.phone = phone
        contact.name = name
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('edit.html', contact=contact)


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    contact = Contact.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/convert')
def convert():
    
    contacts = Contact.query.all()
    for contact in contacts:
        while "  " in contact.phone:
            contact.phone = contact.phone.replace("  ", " ")
        contact.phone = contact.phone.replace("  ", " ").strip()

        while "  " in contact.name:
            contact.name = contact.name.replace("  ", " ")
        contact.name = contact.name.replace("  ", " ").strip()
    db.session.commit()


    law = {
        # viettel
        "016": "03",
        # mobifone
        "0120": "070",
        "0121": "079",
        "0122": "077",
        "0126": "076",
        "0128": "078",
        # vinaphone
        "0124": "084",
        "0127": "081",
        "0129": "082",
        "0123": "083",
        "0125": "085",
        # vietnamobile
        "0186": "056",
        "0188": "058",
        # mobile
        "0199": "059",
    }

    contacts = Contact.query.all()
    for contact in contacts:
        if len(contact.phone) == 11:
            for key in law.keys():
                if contact.phone.startswith(key):

                    new_phone = law[key] + contact.phone[len(key):]

                    existing_contact = Contact.query.filter_by(phone=new_phone).first()
                    if existing_contact:
                        contact.phone = new_phone
                        contact.name = contact.name + " = " + existing_contact.name
                        db.session.delete(existing_contact)
                    else:
                        contact.phone = new_phone

                    db.session.commit()
                    break

    return redirect(url_for('index'))


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    if file and file.filename.endswith('.vcf'):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        _, file_extension = os.path.splitext(filepath)

        contacts = read_vcf(filepath)

        for contact in contacts:
            phone = contact["phone"]
            name = contact["name"]

            while "  " in phone:
                phone = phone.replace("  ", " ")
            phone = phone.replace("  ", " ").strip()

            while "  " in name:
                name = name.replace("  ", " ")
            name = name.replace("  ", " ").strip()

            existing_contact = Contact.query.filter_by(phone=phone).first()
            if not existing_contact:
                new_contact = Contact(phone=phone, name=name)
                db.session.add(new_contact)
                db.session.commit()
            else:
                if name != existing_contact.name:
                    existing_contact.name += f" = {name}"
                    db.session.commit()

    return redirect(url_for('index'))


@app.route('/download/csv')
def download_csv():
    output = io.StringIO()

    writer = csv.writer(output)
    writer.writerow(['ID', 'Phone', 'Name'])

    contacts = Contact.query.all()
    for contact in contacts:
        writer.writerow([contact.id, contact.phone, contact.name])

    output.seek(0)

    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=nghia_contact_manager.csv"}
    )


@app.route('/download/txt')
def download_txt():
    output = io.StringIO()

    output.write('ID\tPhone\tName\n')

    contacts = Contact.query.all()
    for contact in contacts:
        output.write(f'{contact.id}\t{contact.phone}\t{contact.name}\n')

    output.seek(0)

    return Response(
        output.getvalue(),
        mimetype="text/plain",
        headers={"Content-Disposition": "attachment;filename=nghia_contact_manager.txt"}
    )


def to_quoted_printable_hex(s):
    return ''.join(f'={b:02X}' for b in s.encode('utf-8'))


@app.route('/download/vcf')
def download_vcf():
    output = io.StringIO()

    contacts = Contact.query.all()
    for contact in contacts:
        output.write('BEGIN:VCARD\n')
        output.write('VERSION:2.1\n')
        output.write(f'FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:{to_quoted_printable_hex(contact.name)}\n')
        output.write(f'TEL;CELL;PREF:{contact.phone}\n')
        output.write('END:VCARD\n')
        output.write('\n')

    output.seek(0)

    return Response(
        output.getvalue(),
        mimetype="text/vcard",
        headers={"Content-Disposition": "attachment;filename=nghia_contact_manager.vcf"}
    )
