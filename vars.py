# ✨ N I K H I L ✨
# Add your details here and then deploy using Heroku or any platform

import os
from os import environ

# API & Bot Configuration
API_ID = int(environ.get("API_ID", "20619533"))
API_HASH = environ.get("API_HASH", "5893568858a096b7373c1970ba05e296")
BOT_TOKEN = environ.get("BOT_TOKEN", "7270825299:AAGkzGRc1JsLFe_DnTj-A3ZvzxIVK8RzQoM")

# Owner Info
OWNER = int(environ.get("OWNER", "7447651332"))
CREDIT = "SUJAL"

# Authorized Users
AUTH_USER = environ.get('AUTH_USERS', '7447651332').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]

# Ensure OWNER is in AUTH_USERS
if OWNER not in AUTH_USERS:
    AUTH_USERS.append(OWNER)

# Optional Configs
# WEBHOOK = True  # Don’t change this unless needed
# PORT = int(environ.get("PORT", 8080))  # Defaults to 8000 if not set