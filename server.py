# Create the server.py in the virture environment
from flask import Flask, render_template,request, redirect
import csv


app = Flask(__name__)

@app.route("/")
def my_web():
    return render_template('index.html')

@app.route("/index.html")
def home():
    return render_template('index.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/works.html")
def works():
    return render_template('works.html')

@app.route("/work.html")
def work():
    return render_template('work.html')

@app.route("/contact.html")
def contact():
    return render_template('contact.html')

@app.route("/thankyou.html")
def thankyou():
    return render_template('thankyou.html')

# def write_to_file(data):
#     with open('database.txt',mode='a') as database:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = database.write(f'\n{email},{subject},{message}')


# ??? Question -> newline = '' with open('database.csv', newline='', mode='a') as database2:     
def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2,delimiter='|', quotechar='|',quoting=csv.QUOTE_MINIMAL) 
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
#    return 'Form submitted! hoorayyyy!'
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        print(data)
        return redirect('/thankyou.html')
    else:
        return '404! OOPS! something went wrong!'
