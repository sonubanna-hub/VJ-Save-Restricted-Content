import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7625989583:AAGG6LhiIzkavkHgF8PwSGdHsZBkb8puZdM")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "13587863"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "40fadac18a41d7bd704901467733ce00")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6273155665"))

# Your Mongodb Database Url
DB_URI = os.environ.get("DB_URI", "mongodb+srv://sonu5696852349:zupleu7MLZmepEnw@cluster0.uae6h.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
")
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
