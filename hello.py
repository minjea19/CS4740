from flask import Flask, render_template, request, jsonify, abort, make_response
from werkzeug import secure_filename
import os
import subprocess
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world!"

@app.route('/upload')
def uploader():
   print(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates', 'upload.html'))
   return render_template('upload.html')
#   return render_template(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates', 'upload.html'))
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      p = subprocess.Popen(["python", "autograde.py"], stdout=subprocess.PIPE)
      out, err = p.communicate()
      out = out.decode('utf-8').strip('\n')
      return render_template("result.html", result = out)

# PA Assignment 3
temperature = {
            'id': 1,
            'title': u'Room Temperature',
            'current_temp': 70,
            'current_setpoint': 75}


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/governor/api/v1.0/current-temp', methods=['GET'])
def get_current_temp():
    temp = str(temperature['current_temp'])

    return jsonify({'current_temperature': temp})

@app.route('/governor/api/v1.0/current-setpoint/', methods=['GET'])
def get_current_setpoint():
    setpoint = str(temperature['current_setpoint'])
    return jsonify({'current_setpoint': setpoint})


@app.route('/governor/api/v1.0/current-setpoint/<int:temper>', methods=['PUT'])
def set_current_setpoint(temper):
    try:
        temp = request.json['temper']
        temperature['current_setpoint'] = int(temp)

        return jsonify({"Current Temperature is: " + str(temperature['current_setpoint'])})
    except Exception as e:
        print(e)
        not_found(404)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

