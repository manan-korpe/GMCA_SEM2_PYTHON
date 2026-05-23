from flask import Flask, request, redirect, render_template_string
import mysql.connector

p22 = Flask(__name__)

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="event_db"
)

cursor = db.cursor()

@p22.route('/')
def home():
    cursor.execute("SELECT * FROM registrations")
    records = cursor.fetchall()

    html = """
    <html>
    <head>
        <title>Event Registration</title>
    </head>
    <body>
        <h1>Event Registration System</h1>
        <a href='/register'>New Registration</a>
        <br><br>
        <table border='1' cellpadding='10'>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Email</th>
                <th>Phone</th>
                <th>Event Name</th>
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
                    <a href='/cancel/{{row[0]}}'>Cancel Registration</a>
                </td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """
    return render_template_string(html, records=records)


@p22.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        event_name = request.form['event_name']

        sql = """
        INSERT INTO registrations (name, email, phone, event_name)
        VALUES (%s, %s, %s, %s)
        """
        values = (name, email, phone, event_name)

        cursor.execute(sql, values)
        db.commit()

        return redirect('/')

    html = """
    <h2>Event Registration Form</h2>
    <form method='POST'>
        Name:<br>
        <input type='text' name='name' required><br><br>

        Email:<br>
        <input type='email' name='email' required><br><br>

        Phone:<br>
        <input type='text' name='phone' required><br><br>

        Event Name:<br>
        <input type='text' name='event_name' required><br><br>

        <input type='submit' value='Register'>
    </form>
    <br>
    <a href='/'>Back</a>
    """
    return render_template_string(html)


@p22.route('/cancel/<int:id>')
def cancel(id):
    cursor.execute("DELETE FROM registrations WHERE id=%s", (id,))
    db.commit()
    return redirect('/')


if __name__ == '__main__':
    p22.run(debug=True)