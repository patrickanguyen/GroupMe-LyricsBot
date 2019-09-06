import re
import time
import lyricsgenius


class LyricsBot:
    def __init__(self, bot_id: str, client: "Client", genius_token: str):
        self._bot_id = bot_id
        self._client = client
        self._genius = lyricsgenius.Genius(genius_token)

    def post_message(self, text: str, attachs=None):
        """
        Post message on GroupMe
        :param text: text of message
        :param attachs: optional text attachments
        :return:
        """
        self._client.bots.post(self._bot_id, text, attachments=attachs)

    def check_message(self, text=""):
        """
        Check message and output lyrics if message fits
        !lyrics {artist}, {name}
        Returns lyrics, if not do nothing
        :param text: string from GroupMe message
        :return: Bot posts message with lyrics
        """
        lyrics_re = re.match("^!lyrics\s(?P<name>[\S\s]+),\s?(?P<artist>[\S\s]+)$", text)

        if lyrics_re is not None:
            song = self._genius.search_song(lyrics_re.group("name"), lyrics_re.group("artist"))
            # If song is found, print out lyrics
            if song is not None:
                print(song.lyrics)
                lyrics_list = song.lyrics.split("\n\n")
                for line in lyrics_list:
                    self.post_message(line)
                    time.sleep(.500)

            # Else print out error message
            else:
                error_message = "ERROR: No Song Found for {name},{artist}\nFormat is '!lyrics [name], [artist]'".format(artist=lyrics_re.group("artist"), name=lyrics_re.group("name"))
                print(error_message)
                self.post_message(error_message)

