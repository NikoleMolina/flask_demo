from flask import Flask
from flask import render_template, redirect, request, url_for

app = Flask(__name__)

friend_list = [{"name": "Mike Colbert"} ]

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Nikole\'s Friends', friends = friend_list)

@app.route('/nikole')
def mike():
    return render_template('nikole.html', pageTitle='About Nikole')

@app.route('/add_friend', methods=['GET', 'POST'])
def add_friend():
    if request.method == 'POST':
        form = request.form
        fname = form['fname']
        lname = form['lname']
        # email = form['email']
        friend_dict = {"name": fname + " " + lname}
        friend_list.append(friend_dict)
        return redirect(url_for('index'))
    return redirect(url_for('index'))
 

if __name__ == '__main__':
    app.run(debug=True)
