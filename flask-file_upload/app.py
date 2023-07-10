from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == "POST":
        file = request.files['file']
        # Access file properties
        filename = file.filename
        # Save or process the file as needed
        file.save('uploads/' + file.filename)
        # Display success message
        success_message = 'File uploaded successfully'

        # Return a response 
        return render_template('upload.html', success_message=success_message)
    return render_template('upload.html')


if __name__ == "__main__":
    app.run(debug=True)