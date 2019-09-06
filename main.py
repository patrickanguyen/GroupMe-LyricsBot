from groupy import Client
from groupy import exceptions
import time
from LyricsBot import LyricsBot


if __name__ == "__main__":
    access_token = ""
    bot_id = ""
    group_id = ""
    genius_token = ""

    client = Client.from_token(access_token)
    group = client.groups.get(group_id)
    messages = group.messages.list()
    lyricsBot = LyricsBot(bot_id, client, genius_token)

    messages = list(group.messages.list(limit=1))
    message_id = messages[0].id

    while True:
        try:
            # If len of messages greater than 1, process messages, else do nothing
            if len(messages) >= 1:
                for message in messages:
                    # Process message
                    if message.name != "Lyrics Bot" and message.text is not None:
                        lyricsBot.check_message(message.text)

                # Get ID of most recent message
                message_id = messages[0].id
            # Get messages after message_id
            messages = list(group.messages.list_after(message_id=message_id))

        except exceptions.BadResponse:
            print("ERROR")
            client.bots.post(bot_id, "Error with song")

            messages = list(group.messages.list(limit=1))
            message_id = messages[0].id

            time.sleep(5)
