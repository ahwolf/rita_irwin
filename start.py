from flask import Flask
from flask import render_template, jsonify, request
from flask_mail import Mail, Message

app = Flask(__name__)
# app.debug = True
mail = Mail()

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'ritairwin4clerk@gmail.com'
app.config["MAIL_PASSWORD"] = '433beverlyislanddrive'

mail.init_app(app)

@app.route('/')
def hello_world():
    # msg = Message("Hello",
    #               sender="from@example.com",
    #               recipients=["ahwolf@umich.edu"])
    # mail.send(msg)
    return render_template('index.html')


@app.route('/_contact', methods=['GET', 'POST'])
def contact():
    msg = Message("Phone: {phone}\tName: {name}".format(**request.json),
                  sender=request.json["email"],
                  recipients=["ritalynn1756@aol.com",'ritairwin4clerk@gmail.com']
        )
    msg.body = request.json['message']
    mail.send(msg)
    return jsonify(result={"status": 200})

if __name__ == '__main__':
    app.run()