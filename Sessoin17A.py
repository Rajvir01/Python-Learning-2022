# Flask Docs: https://flask.palletsprojects.com/en/2.2.x/

from flask import *

web_app = Flask("HealthLogger")


@web_app.route("/")
def index():

    html_content = """
    <html>
        <title>
             Health Logger App
        </title>
        <body>
            <center>
                <h3>Welcome to Health Logger App
            </center>
        </body>
    </html>
    """

    #return html_content
    return render_template("main.html")

@web_app.route("/welcome")
def welcome():
    #return "You can log health record in th App"
    return render_template("welcome.html")
@web_app.route("/logger")
def logger():
    return render_template("logger.html")

@web_app.route("/logs")
def logs():
    return render_template("logs.html")

@web_app.route("/login")
def login():
    #return "You can log into app"
    return render_template("login.html")

@web_app.route("/register")
def register():
    form_content = """
    <html>
<body>

<h2>HTML Forms</h2>

<form action="/action_page.php">
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname" value="John"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname" value="Doe"><br><br>
  <input type="submit" value="Submit">
</form> 

<p>If you click the "Submit" button, the form-data will be sent to a page called "/action_page.php".</p>

</body>
</html>"""
    #return form_content
    return render_template("register.html")

def main():
    web_app.run()

if __name__ == "__main__":
    main()

