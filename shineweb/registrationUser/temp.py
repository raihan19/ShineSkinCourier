import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('/home/raihan/PycharmProjects/ShineSkin/.env')
load_dotenv(dotenv_path=env_path)

print(os.getenv('EMAIL_USER'))
print(os.environ.get('EMAIL_PASS'))
