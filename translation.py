import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

class Translation(object):
    START_TEXT = f"""<b>Hello there,</b>
    
I am a <b>Mega Link Downloader</b> bot!

Just enter your mega.nz link and I will return the file/video to you!ð

ð  I can set custom captions and custom thumbnails too!

ð  I can download links which are bigger than 2GB too! ð

Press /help for more details!

â¨ <b>A Project By WikiLeaks @TheOnlyMrLucifer</b>"""
    
    DOWNLOAD_START = "ðð¼ðð»ð¹ð¼ð®ð±ð¶ð»ð´ ðð¼ ð ð ð¦ð²ð¿ðð²ð¿ð¥"
    UPLOAD_START = "ð¨ð½ð¹ð¼ð®ð±ð¶ð»ð´ ð§ð¼ ð§ð²ð¹ð²ð´ð¿ð®ðº ð¡ð¼ð  ð¤"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS =  "Downloaded in <b>{}</b> seconds.\n\nUploaded in <b>{}</b> seconds.\n\n<b>Thanks For Using This Free Service</b>"
    SAVED_CUSTOM_THUMB_NAIL = "ððððð¼ðº ð§ðµððºð¯ð»ð®ð¶ð¹ ðð ð¦ð®ðð²ð±. ð§ðµð¶ð ððºð®ð´ð² ðªð¶ð¹ð¹ ðð² ð¨ðð²ð± ðð» ð¬ð¼ðð¿ ð¡ð²ðð ð¨ð½ð¹ð¼ð®ð±ð ð.\n\nIf you want to delete it send\n /deletethumbnail anytime!"
    DEL_ETED_CUSTOM_THUMB_NAIL = "ððððð¼ðº ð§ðµððºð¯ð»ð®ð¶ð¹ ðð¹ð²ð®ð¿ð²ð± ð¦ðð°ð°ð²ððð³ðð¹ð¹ð â.\nYou will now get an auto generated thumbnail for your video uploads!"

    HELP_USER = f"""<b><u>ðHi I am a Mega Link Downloader Bot.. ð</u></b>
 
<u>How to use me:-</u>

<b>Just Send me a mega.nz file link!</b>

<b>Important:-</b> 

- Folder links are not supported and your file should not be bigger than 2GB because I can't upload files which are bigger than 2Gb due to telegram API limits!

- Your link should be valid(not expired or been removed) and should not be password protected or encrypted or private!

âï¸ <b>If you want a custom thumbnail for your uploads send a photo before sending the mega link!.</b> <i>(This step is Optional)</i>

ð  It means it is not necessary to send an image to include as an thumbnail.
If you don't send a thumbnail the video/file will be uploaded with an auto genarated thumbnail from the video.
The thumbnail you send will be used for your next uploads!

press /deletethumbnail if you want to delete the previously saved thumbnail.
(Then the video will be uploaded with an auto-genarated thumbnail!)

âï¸ <b>Special feature</b> :- <i>Set caption to any file you want!</i>

ð  Select an uploaded file/video or forward me <b>Any Telegram File</b> and Just write the text you want to be on the file as a reply to the File by selecting it (as replying to a messageð) and the text you wrote will be attached as caption!ð

Ex:- <a href="https://telegra.ph/file/2eb5419cf242504cca440.jpg">Send Like This! It's Easyð¥³</a>

<b>Note</b> :- You can download links which are bigger than 2GB from me too! Due to telegram API limits I can't upload files which are bigger than 2GB so I will split such files and upload them to you!

â¨ <b>A Project By @SLBotsOfficial</b>"""
