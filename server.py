import os
from main import main
os.environ["SERVER_TYPE"] = 'MAIN_SERVER'
main.run()