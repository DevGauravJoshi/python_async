from channels.generic.websocket import JsonWebsocketConsumer


class ChatConsumer(JsonWebsocketConsumer):
    """
    This consumer is used to show user's online status,
    and send notifications.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)  # Corrected super() call
        self.room_name = None

    def connect(self):
        print("Connected!")
        self.room_name = "home"
        self.accept()
        self.send_json(
            {
                "type": "welcome_message",
                "message": "Hey there! You've successfully connected!",
            }
        )

    def disconnect(self, code):
        print("Disconnected!")
        return super().disconnect(code)
    

    def receive_json(self, content, **kwargs):
        message_type = content["type"]
        if message_type == "greeting":
            print(content["message"])
        return super().receive_json(content, **kwargs)

# My mind is focused on enriching the future, yet there's still a part of me searching for the piece I left behind.
