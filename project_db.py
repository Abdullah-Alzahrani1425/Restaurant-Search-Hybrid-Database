from flask import Flask, render_template_string, request, redirect, url_for, session, flash
from pymongo import MongoClient
import mysql.connector
import bcrypt
import webbrowser
from threading import Timer

app = Flask(__name__)
app.secret_key = 'secret_key'

mysql_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234512345",
    database="restaurant_app"
)
mysql_cursor = mysql_db.cursor()

mysql_cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")
mysql_db.commit()

client = MongoClient("localhost:27017")
db = client["restaurant_db"]
restaurants_collection = db["restaurant"]

login_html = '''
<html><head><title>Login</title></head><body>
<h2>Login</h2>
{% with messages = get_flashed_messages() %}
  {% for msg in messages %}<p>{{ msg }}</p>{% endfor %}
{% endwith %}
<form method="POST" action="/login">
    <input type="email" name="email" placeholder="Email" required><br><br>
    <input type="password" name="password" placeholder="Password" required><br><br>
    <input type="submit" value="Log in">
</form>
<br><a href="/register">Register</a>
</body></html>
'''

@app.route('/')
def home():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password_input = request.form['password'].encode('utf-8')

        mysql_cursor.execute("SELECT password FROM users WHERE email = %s", (email,))
        result = mysql_cursor.fetchone()
        if result and bcrypt.checkpw(password_input, result[0].encode('utf-8')):
            session['user'] = email
            return redirect(url_for('search'))
        else:
            flash("❌ Incorrect login details.")
    return render_template_string(login_html)

register_html = '''
<html><head><title>Register</title></head><body>
<h2>Register</h2>
{% with messages = get_flashed_messages() %}
  {% for msg in messages %}<p>{{ msg }}</p>{% endfor %}
{% endwith %}
<form method="POST" action="/register">
    <input type="email" name="email" placeholder="Email" required><br><br>
    <input type="password" name="password" placeholder="Password" required><br><br>
    <input type="submit" value="Register">
</form>
<br><a href="/login">Login</a>
</body></html>
'''

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password_raw = request.form['password'].encode('utf-8')
        hashed_password = bcrypt.hashpw(password_raw, bcrypt.gensalt()).decode('utf-8')

        try:
            mysql_cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, hashed_password))
            mysql_db.commit()
            flash("✅ Registration successful. You can now log in.")
            return redirect(url_for('login'))
        except mysql.connector.IntegrityError:
            flash("❌ Email already exists.")
    return render_template_string(register_html)

search_html = '''
<html><head><title>Search Restaurants</title></head><body>
<h2>Welcome {{ session['user'] }}</h2>
<h3>Search for Restaurants</h3>
<form method="POST">
    <input type="text" name="query" placeholder="Type restaurant name..." required>
    <input type="submit" value="Search">
</form>
<br>
{% if error_message %}
    <p>{{ error_message }}</p>
{% endif %}
{% if results %}
    <h3>Results:</h3>
    <ul>
        {% for r in results %}
            <li>
                <strong>Name:</strong> {{ r['name'] }}<br>
                <strong>Borough:</strong> {{ r['borough'] }}<br>
                <strong>Cuisine:</strong> {{ r['cuisine'] }}<br>
                <strong>Address:</strong>
                {% if 'address' in r %}
                    {{ r['address'].get('building', '') }} {{ r['address'].get('street', '') }}
                {% else %}
                    Not Available
                {% endif %}
                <br>
                <strong>Grades:</strong>
                <ul>
                    {% for grade in r.get('grades', []) %}
                        <li>{{ grade['date'] }} - Grade: {{ grade['grade'] }} - Score: {{ grade['score'] }}</li>
                    {% endfor %}
                </ul>
            </li>
        {% endfor %}
    </ul>
{% endif %}
<br><a href="/logout">Logout</a>
</body></html>
'''

@app.route('/search', methods=['GET', 'POST'])
def search():
    if 'user' not in session:
        return redirect(url_for('login'))

    results = []
    error_message = None

    if request.method == 'POST':
        query = request.form['query'].lower()
        results = list(restaurants_collection.find({
            "$or": [
                {"name": {"$regex": query, "$options": "i"}},
                {"borough": {"$regex": query, "$options": "i"}},
                {"cuisine": {"$regex": query, "$options": "i"}}
            ]
        }))
        if not results:
            error_message = "❌ No restaurant found with that name."

    return render_template_string(search_html, results=results, error_message=error_message)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(debug=True)
