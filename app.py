from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

messages = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form['message']
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        messages.append({'message': message, 'timestamp': timestamp})
    messages.sort(key=lambda x: x['timestamp'], reverse=True)
    return render_template('index.html.jinja2', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
