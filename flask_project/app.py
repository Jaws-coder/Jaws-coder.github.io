from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Used for session management

# Data stores (in-memory for this example)
site1_users = []
site2_users = []
site3_users = []

# Admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

# Helper function to add user data
def add_user(site, email, password):
    if site == "site1":
        site1_users.append((email, password))
    elif site == "site2":
        site2_users.append((email, password))
    elif site == "site3":
        site3_users.append((email, password))

# Routes for site 1
@app.route('/site1', methods=['GET', 'POST'])
def site1():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        add_user("site1", email, password)
        return redirect(url_for('thank_you', site="Site 1"))
    return render_template('login.html', site="Site 1")

# Routes for site 2
@app.route('/site2', methods=['GET', 'POST'])
def site2():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        add_user("site2", email, password)
        return redirect(url_for('thank_you', site="Site 2"))
    return render_template('login.html', site="Site 2")

# Routes for site 3
@app.route('/site3', methods=['GET', 'POST'])
def site3():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        add_user("site3", email, password)
        return redirect(url_for('thank_you', site="Site 3"))
    return render_template('login.html', site="Site 3")

# Thank you page
@app.route('/thank_you/<site>')
def thank_you(site):
    return f"<h1>Thank you for registering on {site}!</h1>"

# Admin login page
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            return redirect(url_for('admin_panel'))
        else:
            return render_template('admin_login.html', error="Invalid username or password.")
    return render_template('admin_login.html')

# Admin panel
@app.route('/admin')
def admin_panel():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    return render_template('admin.html', site1_users=site1_users, site2_users=site2_users, site3_users=site3_users)

# Admin logout
@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('admin_login'))

if __name__ == '__main__':
    app.run(debug=True)
