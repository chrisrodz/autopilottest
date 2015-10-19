from flask import Flask, request, redirect
import twilio.twiml
import requests
import json

app = Flask(__name__)

headers = {
  'autopilotapikey': 'YOUR API KEY',
  'Content-Type': 'application/json'
}

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""

    data = request.form['Body'].split(' ')
    firstname = data[0]
    lastname = data[1]
    email = data[2]

    data = """
      {
        "contact": {
          "Email": "%s",
          "FirstName": "%s",
          "LastName": "%s"
        }
      }
    """ % (firstname, lastname, email)

    journey_id = "YOUR JOURNEY ID"
    url = "https://api2.autopilothq.com/v1/trigger/%s/contact" % journey_id

    r = requests.post(url, data=data, headers=headers)
    print email
    print r.json()
    resp = twilio.twiml.Response()
    resp.message("Thanks for sending your contact information. We should send you an email shortly")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)