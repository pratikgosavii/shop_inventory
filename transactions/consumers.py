# import json
# from channels.generic.websocket import WebsocketConsumer

# class AlertConsumer(WebsocketConsumer):

#     groups = ['notification_group']

#     def connect(self):
#         self.accept()

#     def disconnect(self, close_code):
#         pass

#     def send_alert(self, event):
#         print(event)
#         message = event['message']

#         # Send the alert message to the WebSocket client
#         self.send(text_data=message)


#     def send_notification(self, message):
#         self.send(text_data=json.dumps({"message": message}))