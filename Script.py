class script(object):
    START_TXT = """๐ป๐๐๐๐ {},
๐ผ ๐๐ ๐ฝ๐ข๐ ๐ก ๐ ๐๐๐๐๐๐ ๐๐๐ - ๐น๐ข๐๐๐ก๐๐๐๐๐ ๐ด๐ข๐ก๐๐๐๐๐ก๐๐ ๐๐๐ก ๐
๐ผ๐ก๐  ๐๐๐๐๐๐ ๐๐ ๐๐ ๐ ๐๐... ๐ฝ๐ข๐ ๐ก ๐ด๐๐ 
๐๐ ๐๐ ๐๐๐ข๐ ๐บ๐๐๐ข๐ ๐ด๐  ๐ด๐๐๐๐,๐โ๐๐ก๐  ๐ด๐๐ ๐ผ ๐๐๐๐ ๐๐๐๐ฃ๐๐๐ ๐๐๐ฃ๐๐๐  ๐โ๐๐๐..๐ฅฐ

ยฉ๏ธMแดษชษดแดแดษชษดแดD Bส: <a href=https://t.me/DARKWEBLOAD>Dแดสแด แดกแดสสแดแดแด๐ฎ๐ณ</a>"""
    HELP_TXT = """๐ท๐ด๐ {}
๐ท๐ด๐๐ด ๐ธ๐ ๐๐ท๐ด ๐ท๐ด๐ป๐ฟ ๐ต๐พ๐ ๐ผ๐ ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐."""
    ABOUT_TXT = """โฏ ๐ผ๐ ๐ฝ๐ฐ๐ผ๐ด: ๐พ๐๐๐๐ ๐๐๐ค๐๐๐ ๐ผ                       
โโโโโโโโโโโโโโโโโโโโ
โโญโโโโโโโโโโโโโโโโฃ 
โโ  ๐ผ๐ ๐ฝ๐ฐ๐ผ๐ด - <a href="http://t.me/Auto_FiLtEr_RoBit_Bot"> ๐พ๐๐๐๐ ๐๐๐ค๐๐๐ ๐ผ</a>
โโ  ๐ฒ๐๐ด๐ฐ๐๐พ๐ - <a href="https://t.me/DARKWEBLOAD">Dแดสแด แดกแดสสแดแดแด๐ฎ๐ณ</a>
โโ  ๐ฒ๐๐ด๐ณ๐ธ๐๐ - <a href="https://t.me/DARKWEBLOAD">DแดกL</a> 
โโ  ๐ป๐ฐ๐ฝ๐ถ๐๐ฐ๐ถ๐ด - แดสสแดษขสแดแด
โโ  ๐ป๐ธ๐ฑ๐๐ฐ๐๐ - แดสแดสแดษด 3
โโ  ๐ฒ๐ป๐พ๐ฝ๐ด๐ณ ๐ต๐๐พ๐ผ - แดแดษดษขแด แดส
โโ  ๐ณ๐ฐ๐๐ฐ ๐ฑ๐ฐ๐๐ด -  สแดสแดแดแด
โโ  ๐ฑ๐๐ธ๐ป๐ณ ๐๐๐ฐ๐๐๐ - แด 1.0.1 [ สแดแดแด ]
โโฐโโโโโโโโโโโโโโโโฃ โโโโโโโโโโโโโโโโโโโโ"""
    SOURCE_TXT = """<b>NOTE:</b>
- This Bot not a open source project. 
- Source - https://t.me/MyGithubSorceCode      

<b>DEVS:</b>
- <a href=https://t.me/DARKWEBLOAD>แฎแแงแฆแแแงแ</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
โข /filter - <code>add a filter in chat</code>
โข /filters - <code>list all the filters of a chat</code>
โข /del - <code>delete a specific filter in chat</code>
โข /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    STICKER_TXT ="""<b>COMMAND /stickerid\n๐จ๐ฟ ๐ธ๐๐ ๐ญ๐พ๐พ๐ฝ ๐ณ๐พ๐๐พ๐๐๐บ๐ ๐ฒ๐๐๐ผ๐๐พ๐ ๐จ๐ฝ ๐ข๐๐๐ผ๐ /stickerid ๐ณ๐ ๐ฆ๐พ๐ ๐ฒ๐๐๐ผ๐๐พ๐ ๐จ๐ฝ (๐ฑ๐พ๐๐๐ ๐ถ๐๐๐ ๐ฒ๐๐๐ผ๐๐พ๐)</b>"""
    CORONA_TXT ="""<b>Here is the help for the coron information module</b>
  /covid <code>(countryname)</code> <b>you can find a corona information of every country</b>

  <b>example</b> : - /covid India"""
     
    TGRAPH_TXT = """Help: <b>TGraph & Paste</b>

Do as you wish with telegra.ph module!

<b>Commands and Usage:</b>
โข /tgmedia or /tgraph - upload supported media (within 5MB) to telegraph.

<b>NOTE:</b>
โข IMDb should have admin privillage.
โข These commands works on both pm and group.
โข These commands can be used by any group member."""

    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- Give a user details

โข/whois :-give a user full details"""
   CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
โข /connect  - <code>connect a particular chat to your PM</code>
โข /disconnect  - <code>disconnect from a chat</code>
โข /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of This bot

<b>Commands and Usage:</b>
โข /id - <code>get id of a specifed user.</code>
โข /info  - <code>get information about a user.</code>
โข /imdb  - <code>get the film information from IMDb source.</code>
โข /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
โข /logs - <code>to get the rescent errors</code>
โข /stats - <code>to get status of files in db.</code>
โข /delete - <code>to delete a specific file from db.</code>
โข /users - <code>to get list of my users and ids.</code>
โข /chats - <code>to get list of the my chats and ids </code>
โข /leave  - <code>to leave from a chat.</code>
โข /disable  -  <code>do disable a chat.</code>
โข /ban  - <code>to ban a user.</code>
โข /unban  - <code>to unban a user.</code>
โข /channel - <code>to get list of total connected channels</code>
โข /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """โ ๐๐พ๐๐ฐ๐ป ๐ต๐ธ๐ป๐ด๐: <code>{}</code>
โ ๐๐พ๐๐ฐ๐ป ๐๐๐ด๐๐: <code>{}</code>
โ ๐๐พ๐๐ฐ๐ป ๐ฒ๐ท๐ฐ๐๐: <code>{}</code>
โ ๐๐๐ด๐ณ ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> ๐ผ๐๐ฑ
โ ๐ต๐๐ด๐ด ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> ๐ผ๐๐ฑ"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
