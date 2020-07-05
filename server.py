from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/<string:page_name>')
def my_page(page_name):
	return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_csv(data)
		return redirect('thankyou.html')
	else:
		return 'something go wrong'

def write_to_csv(data):
	with open('database.csv', newline='', mode='a') as database:
		email = data['Email']
		subject = data['Subject']
		message = data['Message']
		csv_writer = csv.writer(database, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])
		print(email,subject,message)