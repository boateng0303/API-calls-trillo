from flask import Flask, render_template, redirect, url_for
from twilio.rest import Client
from hp import get_character
from open_notify import get_iss_position
from weather import get_weather
import os
import json
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Twilio Configuration
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Route to display the form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle sending the message
@app.route('/send-message', methods=['POST'])
def send_message():
    # Gather data from the APIs
    character_info = get_character()
    iss_info = get_iss_position()
    weather_info = get_weather()

    # Compose the message
    message_body = f"{character_info}\n\n{iss_info}\n\n{weather_info}"

    # Send the message via Twilio
    message = client.messages.create(
        body=message_body,
        from_=TWILIO_PHONE_NUMBER,
        to=MY_PHONE_NUMBER
    )

    # Log the sent message to JSON
    log_message(message_body)

    # After successfully sending the message, redirect to the success page
    return redirect(url_for('success'))

# Function to log messages to a JSON file
def log_message(message):
    log_file = "messages_log.json"
    log_entry = {"message": message}

    if os.path.exists(log_file):
        with open(log_file, "r") as file:
            logs = json.load(file)
    else:
        logs = []

    logs.append(log_entry)

    with open(log_file, "w") as file:
        json.dump(logs, file, indent=4)

# Route to display the success message
@app.route('/success')
def success():
    return render_template('success.html', message="Thank you! Your magical SMS has been sent!")

if __name__ == '__main__':
    app.run(debug=True)
