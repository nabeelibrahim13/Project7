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

# @app.route('/signup', methods=['GET','POST'])
# def signup(methods=['POST']):
#     return render_template("signup.html")
#     # request_data = request.get_json()
#     # new_user = {
#     #             'name': request_data['name'],
#     #             'email': request_data['email'],
#     #             'password': request_data['password']
#     #             }
#     # users.append(new_user)
#     return render_template("signup.html")

@app.route('/signup', methods=['GET','POST'])
def signup():
    return render_template('signup.html')


@app.route('/signupmethod', methods=['GET','POST'])
def signupmethod():
    
    #name = request.form['name']
    new_user = {
                'name': request.form['name'],
                'email': request.form['email'],
                'password': request.form['password']
                }
    users.append(new_user)

    return render_template('signin.html')




@app.route('/signin', methods=['GET','POST'])
def signin():
    return render_template('signin.html')


@app.route('/signinmethod', methods=['GET','POST'])
def signinmethod():
    
    #name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    for user in users:
        if user['email'] == email and user['password'] == password:
            #return jsonify({'message': 'success'})
            data = {'message' : 'success'}
            return render_template('signinstatus.html', data = {'message' : 'success'})
    #return jsonify({'message': 'failure'})
    data = {'message' : 'failure'}
    return render_template('signinstatus.html', data = {'message' : 'failure'} )
#return render_template('index.html', prediction_text=str(result))


@app.route('/showusers', methods=['GET'])
def showusers():
    un=[]
    ue=[]
    cnt = 0
    for user in users:
        cnt+=1
        uname = user['name']
        un.append(uname)
        uemail = user['email']
        ue.append(uemail)
    #abc = ['a','b','c']
    #cnt = len(a)
    #return jsonify({'users': users})
    return render_template('users.html', users = users, un = un, ue = ue, cnt = cnt)



    # for a in users:
    #     n = a.name
    #     e = a.email
    #     data1 = {'name' : n}
    #     data2 = {'email' : e}
    #     return render_template('users.html', data1 = {'name' : n}, data2 = {'email' : e})

    
    



if __name__ == "__main__":
    app.run(debug=True, port = 4001)