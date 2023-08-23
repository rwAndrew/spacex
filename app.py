from flask import Flask, request, jsonify, redirect, url_for

app = Flask(__name__)

user_data = {
    'admin': 'admin',  # 密碼應該是哈希過的
}

def is_authenticated(username, password):
    return username in user_data and user_data[username] == password

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    if is_authenticated(username, password):
        return jsonify(success=True), 200

    return jsonify(success=False), 401

@app.route('/subpage.html')
def subpage():
    username = request.args.get('username')
    password = request.args.get('password')
    
    if is_authenticated(username, password):
        return app.send_static_file('subpage.html')
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
