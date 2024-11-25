"""Todo once we are ready to test in a cloud env"""
# from slack_bolt import App
# from slack_bolt.adapter.socket_mode import SocketModeHandler
#
# # Initialize the app with your bot token and signing secret
# app = App(
#     token="xoxb-your-bot-token",
#     signing_secret="your-signing-secret"
# )
#
# # Listen for messages where the bot is mentioned
# @app.event("app_mention")
# def handle_app_mention(event, say):
#     user = event["user"]
#     text = event["text"]
#     say(f"Hello <@{user}>! You mentioned me with: {text}")
#
# # Listen to direct messages
# @app.event("message")
# def handle_message(event, say):
#     if "subtype" not in event:  # To ignore messages like bot messages
#         user = event["user"]
#         say(f"Hi there, <@{user}>! How can I assist you?")
#
# # Run the app in Socket Mode
# if __name__ == "__main__":
#     handler = SocketModeHandler(app, "xapp-your-socket-mode-token")
#     handler.start()