from flask import Flask, request, redirect, render_template_string
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="addressbook_db"
)

cursor = db.cursor()


@app.route('/')
def home():
    cursor.execute("SELECT * FROM contacts")
    records = cursor.fetchall()

    html = """
    <html>
    <head>
        <title>Address Book</title>
    </head>
    <body>
        <h1>Address Book Application</h1>
        <a href='/add'>Add New Contact</a>
        <br><br>

        <table border='1' cellpadding='10'>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Phone</th>
                <th>Email</th>
                <th>Address</th>
                <th>Action</th>
            </tr>

            {% for row in records %}
            <tr>
                <td>{{row[0]}}</td>
                <td>{{row[1]}}</td>
                <td>{{row[2]}}</td>
                <td>{{row[3]}}</td>
                <td>{{row[4]}}</td>
                <td>
                    <a href='/edit/{{row[0]}}'>Modify</a>
                    &nbsp;&nbsp;
                    <a href='/delete/{{row[0]}}'>Delete</a>
                </td>
            </tr>
            {% endfor %}

        </table>
    </body>
    </html>
    """

    return render_template_string(html, records=records)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        address = request.form['address']

        sql = """
        INSERT INTO contacts (name, phone, email, address)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(sql, (name, phone, email, address))
        db.commit()

        return redirect('/')

    html = """
    <h2>Add Contact</h2>
    <form method='POST'>
        Name:<br>
        <input type='text' name='name' required><br><br>

        Phone:<br>
        <input type='text' name='phone' required><br><br>

        Email:<br>
        <input type='email' name='email' required><br><br>

        Address:<br>
        <textarea name='address' required></textarea><br><br>

        <input type='submit' value='Save'>
    </form>
    <br>
    <a href='/'>Back</a>
    """

    return render_template_string(html)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        address = request.form['address']

        sql = """
        UPDATE contacts
        SET name=%s, phone=%s, email=%s, address=%s
        WHERE id=%s
        """

        cursor.execute(sql, (name, phone, email, address, id))
        db.commit()

        return redirect('/')

    cursor.execute("SELECT * FROM contacts WHERE id=%s", (id,))
    row = cursor.fetchone()

    html = """
    <h2>Modify Contact</h2>
    <form method='POST'>
        Name:<br>
        <input type='text' name='name' value='{{row[1]}}' required><br><br>

        Phone:<br>
        <input type='text' name='phone' value='{{row[2]}}' required><br><br>

        Email:<br>
        <input type='email' name='email' value='{{row[3]}}' required><br><br>

        Address:<br>
        <textarea name='address' required>{{row[4]}}</textarea><br><br>

        <input type='submit' value='Update'>
    </form>
    <br>
    <a href='/'>Back</a>
    """

    return render_template_string(html, row=row)


@app.route('/delete/<int:id>')
def delete(id):
    cursor.execute("DELETE FROM contacts WHERE id=%s", (id,))
    db.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)