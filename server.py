import os
from app import app
os.environ["SERVER_TYPE"] = 'MAIN_SERVER'
app.run()
