from flask import Flask, render_template, request
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
		
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

