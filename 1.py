from flask import Flask, render_template, flash, url_for, redirect,session, request, make_response
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = b'17fe24bcaf16dffcc795606c2e0e0ebf986e8dc5aeccfecd287e4334cbcca37f'

@app.route('/form/', methods=['GET', 'POST'])
def form():
    session.pop('name',None)
    return render_template('form.html')

@app.route('/submit/', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        session ['name'] = request.form.get('name')
    return render_template('flash_form.html')


if __name__ == '__main__':
    app.run(debug=True)