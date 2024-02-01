from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__, template_folder='templates')
app.secret_key = 'your_secret_key'  # Change this to a secure secret key

# Define routes for different pages
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movies')
def movies():
    return render_template('movies.html')

@app.route('/games')
def games():
    return render_template('games.html')

@app.route('/webseries')
def webseries():
    return render_template('webseries.html')

@app.route('/music')
def music():
    return render_template('music.html')

# File Handling Example
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an empty file without a filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            # Save the uploaded file to a designated folder
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            flash('File uploaded successfully')
            return redirect(url_for('index'))
    return render_template('upload.html')

# Error Handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = 'uploads'  # Create an 'uploads' folder in your project directory
    app.run(debug=True)
