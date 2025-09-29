
# from flask import Flask, render_template, request, redirect, url_for
# import mysql.connector

# app = Flask(__name__)


# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="rayna@22*", 
#     database="todo_flask"
# )
# cursor = conn.cursor(dictionary=True) 


# @app.route('/')
# def home():
#     cursor.execute("SELECT * FROM tasks")
#     tasks = cursor.fetchall()
#     return render_template('index.html', tasks=tasks)


# @app.route('/add', methods=['POST'])
# def add():
#     task = request.form['task']
#     due = request.form['due']
#     priority = request.form['priority']
#     cursor.execute("INSERT INTO tasks (task, due, priority) VALUES (%s, %s, %s)", (task, due, priority))
#     conn.commit()
#     return redirect(url_for('home'))


# @app.route('/delete/<int:id>')
# def delete(id):
#     cursor.execute("DELETE FROM tasks WHERE id = %s", (id,))
#     conn.commit()
#     return redirect(url_for('home'))

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request, redirect, url_for, session
# import mysql.connector
# from datetime import datetime

# app = Flask(__name__)
# app.secret_key = 'rayna_super_secret_key'  # needed for session

# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="rayna@22*",  
#     database="todo_flask"
# )
# cursor = conn.cursor(dictionary=True)

# VALID_USERNAME = "rayna"
# VALID_PASSWORD = "12345"

# @app.route('/')
# def login():
#     return render_template('login.html')

# @app.route('/login', methods=['POST'])
# def do_login():
#     username = request.form['username']
#     password = request.form['password']

#     if username == VALID_USERNAME and password == VALID_PASSWORD:
#         session['user'] = username
#         login_time = datetime.now()
#         cursor.execute("INSERT INTO logins (username, login_time) VALUES (%s, %s)", (username, login_time))
#         conn.commit()
#         return redirect(url_for('home'))
#     else:
#         return render_template('login.html', error="Invalid credentials")

# @app.route('/home')
# def home():
#     if 'user' not in session:
#         return redirect(url_for('login'))
    
#     cursor.execute("SELECT * FROM tasks")
#     tasks = cursor.fetchall()
#     return render_template('index.html', tasks=tasks)

# @app.route('/add', methods=['POST'])
# def add():
#     if 'user' not in session:
#         return redirect(url_for('login'))

#     task = request.form['task']
#     due = request.form['due']
#     priority = request.form['priority']
#     cursor.execute("INSERT INTO tasks (task, due, priority) VALUES (%s, %s, %s)", (task, due, priority))
#     conn.commit()
#     return redirect(url_for('home'))

# @app.route('/delete/<int:id>')
# def delete(id):
#     if 'user' not in session:
#         return redirect(url_for('login'))

#     cursor.execute("DELETE FROM tasks WHERE id = %s", (id,))
#     conn.commit()
#     return redirect(url_for('home'))

# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect(url_for('login'))

# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask, render_template, request, redirect, url_for, session
# import mysql.connector
# from datetime import datetime

# app = Flask(__name__)
# app.secret_key = 'super_secure_rayna_key'

# #  MySQL connection
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="rayna@22*",  
#     database="todo_flask"
# )
# cursor = conn.cursor(dictionary=True)

# # login
# @app.route('/')
# def login():
#     return render_template('login.html')

# @app.route('/login', methods=['POST'])
# def do_login():
#     username = request.form['username']
#     password = request.form['password']

#     cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
#     user = cursor.fetchone()

#     if user:
#         session['user'] = username
#         session['is_admin'] = user['is_admin']
#         login_time = datetime.now()
#         cursor.execute("INSERT INTO logins (username, login_time) VALUES (%s, %s)", (username, login_time))
#         conn.commit()
#         return redirect(url_for('home'))
#     else:
#         return render_template('login.html', error="Invalid username or password.")

# # signup
# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']

#         cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
#         if cursor.fetchone():
#             return render_template('signup.html', error="Username already exists.")

#         cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
#         conn.commit()
#         return redirect(url_for('login'))

#     return render_template('signup.html')

# # forgot password
# @app.route('/forgot', methods=['GET', 'POST'])
# def forgot():
#     if request.method == 'POST':
#         username = request.form['username']
#         new_password = request.form['new_password']

#         cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
#         if not cursor.fetchone():
#             return render_template('forgot.html', error="Username not found.")

#         cursor.execute("UPDATE users SET password = %s WHERE username = %s", (new_password, username))
#         conn.commit()
#         return redirect(url_for('login'))

#     return render_template('forgot.html')

# # home
# @app.route('/home')
# def home():
#     if 'user' not in session:
#         return redirect(url_for('login'))

#     cursor.execute("SELECT * FROM tasks WHERE username = %s", (session['user'],))
#     tasks = cursor.fetchall()
#     return render_template('index.html', tasks=tasks)

# # add task
# @app.route('/add', methods=['POST'])
# def add():
#     if 'user' not in session:
#         return redirect(url_for('login'))

#     task = request.form['task']
#     due = request.form['due']
#     priority = request.form['priority']
#     status = request.form['status']
#     username = session['user']

#     cursor.execute(
#         "INSERT INTO tasks (task, due, priority, status, username) VALUES (%s, %s, %s, %s, %s)",
#         (task, due, priority, status, username)
#     )
#     conn.commit()
#     return redirect(url_for('home'))

# # edit task
# @app.route('/edit/<int:id>')
# def edit(id):
#     if 'user' not in session:
#         return redirect(url_for('login'))

#     cursor.execute("SELECT * FROM tasks WHERE id = %s", (id,))
#     task = cursor.fetchone()

#     if task and (task['username'] == session['user'] or session.get('is_admin')):
#         return render_template('edit.html', task=task)
#     else:
#         return redirect(url_for('home'))

# @app.route('/update/<int:id>', methods=['POST'])
# def update(id):
#     if 'user' not in session:
#         return redirect(url_for('login'))

#     task = request.form['task']
#     due = request.form['due']
#     priority = request.form['priority']
#     status = request.form['status']

#     cursor.execute(
#         "UPDATE tasks SET task=%s, due=%s, priority=%s, status=%s WHERE id=%s",
#         (task, due, priority, status, id)
#     )
#     conn.commit()
#     return redirect(url_for('home'))

# # delete task
# @app.route('/delete/<int:id>')
# def delete(id):
#     if 'user' not in session:
#         return redirect(url_for('login'))

#     # Only admin can delete
#     cursor.execute("SELECT * FROM tasks WHERE id = %s", (id,))
#     task = cursor.fetchone()

#     if task and (task['username'] == session['user'] or session.get('is_admin')):
#         cursor.execute("DELETE FROM tasks WHERE id = %s", (id,))
#         conn.commit()

#     return redirect(url_for('home'))

# # admin
# @app.route('/admin')
# def admin_panel():
#     if 'user' not in session or not session.get('is_admin'):
#         return redirect(url_for('home'))

#     cursor.execute("SELECT username, is_admin, created_at FROM users")
#     users = cursor.fetchall()

#     cursor.execute("SELECT * FROM tasks")
#     tasks = cursor.fetchall()

#     return render_template('admin.html', users=users, tasks=tasks)

# # logout
# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect(url_for('login'))

# # main
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'super_secure_rayna_key'

# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rayna@22*",
    database="todo_flask"
)
cursor = conn.cursor(dictionary=True)

# Home/Login redirect
@app.route('/')
def root():
    return redirect('/login')

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()
        if user:
            session['username'] = user['username']
            session['user_id'] = user['id']
            session['is_admin'] = user['is_admin']
            cursor.execute("INSERT INTO logins (username, login_time) VALUES (%s, %s)", (username, datetime.now()))
            conn.commit()
            return redirect('/dashboard')
            
        else:
            flash("Invalid username or password", "danger")
    return render_template('login.html')


# Signup
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor.execute("INSERT INTO users (username, password, is_admin) VALUES (%s, %s, %s)", (username, password, False))
        conn.commit()
        flash("Account created successfully! Please login.", "success")
        return redirect('/login')
    return render_template('signup.html')

# Dashboard
@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect('/login')
    cursor.execute("SELECT * FROM tasks WHERE user_id = %s", (session['user_id'],))
    tasks = cursor.fetchall()
    return render_template('index.html', tasks=tasks)

# Add Task
@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    due = request.form['due']
    priority = request.form['priority']
    cursor.execute("INSERT INTO tasks (task, due, priority, status, user_id) VALUES (%s, %s, %s, %s, %s)",
                   (task, due, priority, 'Pending', session['user_id']))
    conn.commit()
    return redirect('/dashboard')


# Delete Task
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    cursor.execute("DELETE FROM tasks WHERE id=%s AND user_id=%s", (id, session['user_id']))
    conn.commit()
    return redirect('/dashboard')

# Update Status
# @app.route('/update/<int:id>', methods=['POST'])
# def update(id):
#     status = request.form['status']
#     cursor.execute("UPDATE tasks SET status=%s WHERE id=%s AND user_id=%s", (status, id, session['user_id']))
#     conn.commit()
#     return redirect('/dashboard')
@app.route('/update_status/<int:id>', methods=['POST'])
def update_status(id):
    if 'user_id' not in session:
        return redirect('/login')

    new_status = request.form['status']
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status = %s WHERE id = %s AND user_id = %s", (new_status, id, session['user_id']))
    conn.commit()
    return redirect('/dashboard')


# Forgot Password
@app.route('/forgot', methods=['GET', 'POST'])
def forgot():
    if request.method == 'POST':
        username = request.form['username']
        return redirect(url_for('reset_password', username=username))  # redirects to reset
    return render_template('forgot.html')



# Reset Password
@app.route('/reset/<username>', methods=['GET', 'POST'])
def reset_password(username):
    if request.method == 'POST':
        new_password = request.form['password']
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET password=%s WHERE username=%s", (new_password, username))
        conn.commit()
        return redirect(url_for('login'))  # goes to login page
    return render_template('reset.html')


# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)






# from flask import Flask, render_template, request, redirect, url_for, session, flash
# import mysql.connector
# from datetime import datetime

# app = Flask(__name__)
# app.secret_key = 'super_secure_rayna_key'

# # MySQL connection
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="rayna@22*",
#     database="todo_flask"
# )
# cursor = conn.cursor(dictionary=True)

# # root
# @app.route('/')
# def root():
#     return redirect('/login')

# # login
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
#         user = cursor.fetchone()
#         if user:
#             session['username'] = user['username']
#             session['user_id'] = user['id']
#             session['is_admin'] = user['is_admin']
#             cursor.execute("INSERT INTO logins (username, login_time) VALUES (%s, %s)", (username, datetime.now()))
#             conn.commit()
#             return redirect('/category')
#         else:
#             flash("Invalid username or password", "danger")
#     return render_template('login.html')

# # signup
# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         cursor.execute("INSERT INTO users (username, password, is_admin) VALUES (%s, %s, %s)", (username, password, False))
#         conn.commit()
#         flash("Account created successfully! Please login.", "success")
#         return redirect('/login')
#     return render_template('signup.html')

# # select cat
# @app.route('/category')
# def choose_category():
#     if 'username' not in session:
#         return redirect('/login')
#     return render_template('choose_category.html')

# # cateegory dash
# @app.route('/dashboard/<category>')
# def dashboard(category):
#     if 'username' not in session:
#         return redirect('/login')
#     cursor.execute("SELECT * FROM tasks WHERE user_id = %s AND category = %s", (session['user_id'], category))
#     tasks = cursor.fetchall()
#     return render_template('index.html', tasks=tasks, category=category)

# # add task
# @app.route('/add/<category>', methods=['POST'])
# def add_task(category):
#     if 'user_id' not in session:
#         return redirect('/login')
#     task = request.form['task']
#     due = request.form['due']
#     priority = request.form['priority']
#     cursor.execute("INSERT INTO tasks (task, due, priority, status, user_id, category) VALUES (%s, %s, %s, %s, %s, %s)",
#                    (task, due, priority, 'Pending', session['user_id'], category))
#     conn.commit()
#     return redirect(f'/dashboard/{category}')

# # dlt task
# @app.route('/delete/<int:id>/<category>', methods=['POST'])
# def delete(id, category):
#     cursor.execute("DELETE FROM tasks WHERE id=%s AND user_id=%s", (id, session['user_id']))
#     conn.commit()
#     return redirect(f'/dashboard/{category}')

# # update
# @app.route('/update_status/<int:id>/<category>', methods=['POST'])
# def update_status(id, category):
#     if 'user_id' not in session:
#         return redirect('/login')
#     new_status = request.form['status']
#     cursor.execute("UPDATE tasks SET status = %s WHERE id = %s AND user_id = %s", (new_status, id, session['user_id']))
#     conn.commit()
#     return redirect(f'/dashboard/{category}')

# # forgot pswd
# @app.route('/forgot', methods=['GET', 'POST'])
# def forgot():
#     if request.method == 'POST':
#         username = request.form['username']
#         return redirect(url_for('reset_password', username=username))
#     return render_template('forgot.html')

# # reset pswd
# @app.route('/reset/<username>', methods=['GET', 'POST'])
# def reset_password(username):
#     if request.method == 'POST':
#         new_password = request.form['password']
#         cursor.execute("UPDATE users SET password=%s WHERE username=%s", (new_password, username))
#         conn.commit()
#         flash("Password reset successfully!", "success")
#         return redirect('/login')
#     return render_template('reset.html')

# # logout
# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect('/login')





# if __name__ == '__main__':
#     app.run(debug=True)
