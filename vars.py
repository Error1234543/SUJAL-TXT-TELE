#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "20619533"))
API_HASH = environ.get("5893568858a096b7373c1970ba05e296", "5de9fd033aa828dfd3bf0c28adeee660")
BOT_TOKEN = environ.get("BOT_TOKEN", "7270825299:AAGkzGRc1JslFe_DnTj-A3ZvzxIVK8RzQoM")
OWNER = int(environ.get("OWNER", "7447651332"))
CREDIT = "SUJAL"
AUTH_USER = os.environ.get('AUTH_USERS', '6883471516').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
