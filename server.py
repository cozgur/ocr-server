import os
from app import app
os.environ["SERVER_TYPE"] = 'MAIN_SERVER'
app.run("0.0.0.0", 8000, debug=True)