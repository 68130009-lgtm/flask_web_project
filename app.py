from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tech')
def tech():
    return render_template('tech.html')

@app.route('/myid')
def myid():
    return "รหัสนักศึกษา: 68130009"

@app.route('/draw/<int:num>')
def draw(num):
    result = ""
    for i in range(num):
        result += f"แถวที่ {i+1}: xxxx<br>"
    return result

if __name__ == '__main__':
    app.run(debug=True)
