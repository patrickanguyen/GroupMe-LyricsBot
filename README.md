# GroupMe-LyricsBot
A GroupMe bot that returns the lyrics of songs

## Requirements
A [GroupMe](https://dev.groupme.com/) and [Genius](https://genius.com/developers) account is required in order to run the bot.

In addition, you need to install GroupyAPI and LyricsGenius.
```
pip install GroupyAPI
```
```
pip install lyricsgenius
```


## Starting the bot

### Creating the bot
Go to https://dev.groupme.com/bots and create a bot in your respective group chat.

### Editing the variables
Next, you must first edit the variables in main.py
* access_token - Your GroupMe access token which can be obtained at https://dev.groupme.com/
* bot_id - The bot id which is displayed next to the bot's name at https://dev.groupme.com/bots
* group_id - The group id which is also displayed at https://dev.groupme.com/bots
* genius_token - Your Genius Client Access Token, which is available at https://genius.com/api-clients

After editing the variables, just run main.py and you're all set!

## Using the bot
```
!lyrics {name}, {artist}
```
Simply replace the fields with your song name and artist and the bot will send the songs lyrics.

The bot sends a single message for each verse, so longer songs can be quite spammy, so please be cautious.

### Understanding error messages
```
ERROR: No Song Found for {name},{artist}
Format is '!lyrics [name], [artist]'
```
The Genius API could not find a song that matched the song's description so recheck the spelling of the song's name and artist,
then try again.
```
Error with song
```
The Genius API found the song, but the LyricsBot could not output the lyrics for a certain reason.
The reason behind this error can be quite broad, but a common reason is that the verse of the song is too long for the GroupMe character limit.

If you get this suggestion, the best option is to choose another song. 
