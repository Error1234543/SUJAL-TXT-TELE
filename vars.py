#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "26330942"))
API_HASH = environ.get("API_HASH", "5de9fd033aa828dfd3bf0c28adeee660")
BOT_TOKEN = environ.get("BOT_TOKEN", "7855577752:AAFKQfqK9SOlQxPE5NPJrJrPFK6xjXOFZ8Y")
OWNER = int(environ.get("OWNER", "6883471516"))
CREDIT = "SUJAL"
AUTH_USER = os.environ.get('AUTH_USERS', '6883471516').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
