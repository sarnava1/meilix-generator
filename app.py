from flask import Flask, render_template
import os
import git
import subprocess

# cloning meilix code
#os.system("git clone https://github.com/fossasia/meilix.git")

app = Flask(__name__)

@app.route('/')
def index():
	#Index page
	return render_template("index.html")

#Function to call meilix script on clicking the build button	
def meilixCall():
    subprocess.call(['./build.sh'])

@app.route('/about')
def about():
	#About page
	return render_template("about.html")

#Return a custom 404 error.
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def application_error(e):
    #Return a custom 500 error.
    return 'Sorry, unexpected error: {}'.format(e), 500


if __name__ == '__main__':
    app.run()
