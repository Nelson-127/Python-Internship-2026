from flask import Flask, render_template, request

from forms import ContactForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "rwasgdfng"
messages = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    technologies = [
        {
            "title": "Web Development",
            "description": "Modern responsive web applications using scalable architectures."
        },

        {
            "title": "Cybersecurity",
            "description": "Security-first infrastructure and application protection systems."
        },

        {
            "title": "AI Integration",
            "description": "Intelligent automation and AI-powered digital workflows."
        },

        {
            "title": "Cloud Infrastructure",
            "description": "Reliable cloud-native deployment and scalable backend architecture."
        }
    ]

    return render_template(
        "about.html",
        technologies=technologies
    )


@app.route("/projects")
def projects():
    projects_data = [

        {
            "title": "AI Dashboard",
            "description": "Analytics platform with intelligent monitoring systems.",
            "status": "Active"
        },

        {
            "title": "Cybersecurity Platform",
            "description": "Security-focused infrastructure management interface.",
            "status": "Development"
        },

        {
            "title": "Cloud Automation",
            "description": "Automated deployment and scalable backend workflows.",
            "status": "Completed"
        },

        {
            "title": "Data Visualization",
            "description": "Interactive dashboards and system reporting tools.",
            "status": "Active"
        }

    ]

    return render_template(
        "projects.html",
        projects=projects_data
    )


@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        data = {
            "name": form.name.data,
            "email": form.email.data,
            "message": form.message.data
        }

        messages.append(data)

        print(messages)

    return render_template("contact.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
