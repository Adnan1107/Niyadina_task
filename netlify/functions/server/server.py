import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'work.settings')

from mangum import Mangum
from work.asgi import application

handler = Mangum(application, lifespan="off")
