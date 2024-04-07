from flask import Flask, request

app = Flask(__name__)

@app.post('/upload')
def upload():
    if file_storage := request.files.get('file'):
        file_storage.save('files/' + file_storage.filename)
    return ""

@app.route('/')
def index():
    return """
<html>
    <body>
        <form method='POST' action='/upload' enctype='multipart/form-data'>
            <input type='file' name='file'><br>
            <input type='submit' value='Upload'><br>
        </form>
    </body>
</html>
    """

app.run('0.0.0.0', port=8080)

