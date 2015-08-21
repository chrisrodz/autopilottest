from flask import Flask, request, redirect
import twilio.twiml
import requests
import json

app = Flask(__name__)

headers = {
  'autopilotapikey': '1f2db1452163468eb11a75241eaa74ca',
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
    import pdb; pdb.set_trace()
    print email
    print r.json()
    resp = twilio.twiml.Response()
    resp.message("Thanks for sending your email address. We should send you an email shortly")



    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)