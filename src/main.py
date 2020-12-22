import uvicorn
import sys, getopt

from app import app
from configparser import ConfigParser


def main(argv: list() = sys.argv):
    """
    reload 옵션과 PORT를 지정해주는 함수
    """

    config = ConfigParser()
    config.read("../config.ini")

    FILE_NAME = argv[0]
    reload: str = "False"
    try:
        PORT: int = int(config.get("DEFAULT", "PORT"))
    except Exception as e:
        print(e)
        PORT = 5252

    try:
        opts, _etc_args = getopt.getopt(argv[1:], "HRP:", ["reload", "PORT="])

    except getopt.GetoptError:
        print(FILE_NAME, "-R -P <Port Number>")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-H", "--help"):
            print(FILE_NAME, "-R -P <Port Number>")
            sys.exit(2)
        elif opt in ("-R", "--reload"):
            reload: str = "True"
            # "reload setting option : -R, --reload"
        elif opt in ("-P", "--PORT"):
            PORT: int = int(arg)
            # "PORT setting option : -P args, --PORT=args"
    uvicorn.run("app:app", port=PORT, reload=reload)


if __name__ == "__main__":
    main(sys.argv)
