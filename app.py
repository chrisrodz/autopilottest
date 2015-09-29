from flask import Flask, request, redirect
import twilio.twiml
import requests
import json

app = Flask(__name__)

headers = {
  'autopilotapikey': '9e19dcb628374f429b6d48f22466acac',
  'Content-Type': 'application/json'
}

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""

    email = request.form['Body']

    data = """
      {
        "contact": {
          "Email": "%s"
        }
      }
    """ % email

    r = requests.post('https://api2.autopilothq.com/v1/trigger/0001/contact', data=data, headers=headers)
    print email
    print r.json()
    resp = twilio.twiml.Response()
    resp.message("Thanks for sending your email address. We should send you an email shortly")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)