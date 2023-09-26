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
def index():
    return render_template("about.html")

@app.route('/signup', methods=['GET','POST'])
def signup(methods=['POST']):
    return render_template("signup.html")
    # request_data = request.get_json()
    # new_user = {
    #             'name': request_data['name'],
    #             'email': request_data['email'],
    #             'password': request_data['password']
    #             }
    # users.append(new_user)
    return render_template("signup.html")


@app.route('/signin', methods=['GET','POST'])
def signin():
    return render_template('signin.html')
    # render_template("signin.html")
    # request_data = request.get_json()
    # for user in users:
    #     if user['email'] == request_data['email'] and user['password'] == request_data['password']:
    #         return jsonify({'message': 'success'})
    # return jsonify({'message': 'failure'})

@app.route('/showusers', methods=['GET'])
def showusers():
    return jsonify({'users': users})



if __name__ == "__main__":
    app.run(debug=True, port = 4001)