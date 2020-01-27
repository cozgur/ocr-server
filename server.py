import os
from app import app
os.environ["SERVER_TYPE"] = 'MAIN_SERVER'
app.run(host="0.0.0.0", port=8000, debug=True)
