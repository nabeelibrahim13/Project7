from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

users = [
    {
        'name': 'John',
        'email': 'john@abc.com',
        'password': 'john123'
    },
    {
        'name': 'Smith',
        'email': 'smith@abc.com',
        'password': 'smith123'
    },
]


@app.route('/')
def home():
    return render_template('home.html')

@app.route("/signup", methods=['POST'])
def signup():
    request_data = request.get_json()
    new_user = {
                'name': request_data['name'],
                'email': request_data['email'],
                'password': request_data['password']
                }
    users.append(new_user)
    return jsonify({'users': users})


@app.route('/signin/', methods=['POST'])
def signin():
    request_data = request.get_json()
    for user in users:
        if user['email'] == request_data['email'] and user['password'] == request_data['password']:
            return jsonify({'message': 'success'})
    return jsonify({'message': 'failure'})

@app.route('/showusers', methods=['GET'])
def showusers():
    return jsonify({'users': users})



if __name__ == "__main__":
    app.run(debug=True)