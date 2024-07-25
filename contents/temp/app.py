# pip install flask
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Danh sách công việc mẫu
tasks = [
    {'id': 1, 'title': 'Làm việc nhà', 'description': 'Rửa chén, quét nhà'},
    {'id': 2, 'title': 'Đi chợ', 'description': 'Mua rau, thịt, cá'},
]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        new_task = {
            'id': len(tasks) + 1,
            'title': title,
            'description': description
        }
        tasks.append(new_task)
        return redirect(url_for('index'))

@app.route('/update/<int:task_id>', methods=['GET', 'POST'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if request.method == 'POST':
        task['title'] = request.form['title']
        task['description'] = request.form['description']
        return redirect(url_for('index'))
    return render_template('update.html', task=task)

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
