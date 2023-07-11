from flask import Flask, request
from messengerbot import MessengerClient, messages, attachments

# Initialize Flask app
app = Flask(__name__)

# Initialize MessengerClient with your Facebook Page Access Token
page_access_token = 'your_page_access_token'
messenger = MessengerClient(page_access_token)

# Define a route for receiving webhook events
@app.route('/webhook', methods=['POST'])
def webhook():
    # Parse incoming messages
    messenger.parse_webhook(request.get_data(as_text=True))

    # Handle incoming messages
    for event in messenger.get_events():
        if isinstance(event, messages.MessageEvent):
            sender_id = event.sender_id
            message_text = event.message.text

            # Process the received message
            response_text = process_message(message_text)

            # Send a response back to the user
            messenger.send_text_message(sender_id, response_text)

    return 'OK'

# Process the received message
def process_message(message_text):
    # Add your custom logic here to process the message
    # and generate an appropriate response
    response_text = 'Hello! You said: ' + message_text
    return response_text

# Run the Flask app
if __name__ == '__main__':
    app.run()
