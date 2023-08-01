from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Scientist',
    'location': 'Nairobi, Kenya',
    'salary': 'Kes. 100, 000'
  },
  {
    'id': 2,
    'title': 'Data Analyst',
    'location': 'Kisumu, Kenya',
    'salary': 'Kes. 70, 000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 'Kes. 50, 000'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Mombasa, Kenya',
    'salary': 'Kes. 80, 000'
  },
  {
    'id': 5,
    'title': 'DevOps Engineer',
    'location': 'Remote',
    #'salary': 'Kes. 100, 000'
  }
]


@app.route("/")
def hello():
  return render_template('home.html', jobs=JOBS, company_name='Abiollagh')


@app.route("/api/jobs")
def job_list():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
