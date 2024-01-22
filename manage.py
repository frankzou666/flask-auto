

from flask_auto import create_app
from config import Config

def main():

    app=create_app()
    app.run(host=Config.HOST,port=Config.port)


if __name__=="__main__":
    main()