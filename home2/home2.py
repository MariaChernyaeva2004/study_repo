from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/table/<sex>/<int:age>")
def table(sex, age):
    if "female" in sex.lower():
        if age < 21:
            return render_template("table.html",
                                   title="Марсианин",
                                   path_to_image=url_for("static",
                                                         filename="img/blue.jpeg"),
                                   path_to_image_2=url_for("static",
                                               filename="img/kids.jpg"))

        else:
            return render_template("table.html",
                                   title="Марсианин",
                                   path_to_image=url_for("static",
                                                         filename="img/dark.jpg"),
                                   path_to_image_2=url_for("static",
                                                           filename="img/adult.png"))
    if "male" in sex.lower():
        if age < 21:
            return render_template("table.html",
                                   title="Марсианка",
                                   path_to_image=url_for("static",
                                                         filename="img/pink.jpg"),
                                   path_to_image_2=url_for("static",
                                                         filename="img/kids.jpg"))

        else:
            return render_template("table.html",
                                   title="Марсианка",
                                   path_to_image=url_for("static",
                                                         filename="img/red.jpg"),
                                   path_to_image_2=url_for("static",
                                               filename="img/adult.png"))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
