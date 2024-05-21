from dotenv import load_dotenv
import os

load_dotenv(".env")

BOT_TOKEN = os.environ.get("BOT_TOKEN")
PROVIDER_TOKEN_CLICK = os.environ.get('PROVIDER_TOKEN_CLICK')
PROVIDER_TOKEN_PAYME = os.environ.get('PROVIDER_TOKEN_PAYME')
