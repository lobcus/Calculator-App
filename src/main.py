from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', title="Main")


@app.route("/about")
def about():
    return render_template('about.html', title="About")

# we can store some of our future projects here
@app.route("/future-projects")
def future():
    return render_template('future.html', title="Future Projects")

if __name__ == '__main__':
    app.run(debug=True)
