from flask import Flask, render_template, request, flash
import csv

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def load_courses():
    courses = []
    with open('data.txt', 'r') as file:
        reader = csv.reader(file, delimiter='|')
        for row in reader:
            course = {
                'code': row[0].strip(),
                'name': row[1].strip(),
                'credits': int(row[2].strip())
            }
            courses.append(course)
    return courses

@app.route('/', methods=['GET', 'POST'])
def credit_calculator():
    if request.method == 'POST':
        dropdown_values = []
        for i in range(8):
            dropdown_values.append(request.form.get('dropdown{}'.format(i)))

        total_credits = 0
        for value in dropdown_values:
            if value.isdigit():
                total_credits += int(value)

        if total_credits < 24:
            flash("Need {} credits to complete the target".format(24 - total_credits))
        else:
            flash("Congratulations! You have met the credit requirements.")

    courses = load_courses()
    return render_template('index.html', courses=courses)

if __name__ == '__main__':
    app.run()
