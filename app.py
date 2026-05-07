from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def register():
    message = ""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            message = "All fields are required!"
        else:
            message = f"User '{username}' created successfully!"

    return render_template("register.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)

