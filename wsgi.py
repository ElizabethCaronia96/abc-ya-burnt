import importlib
projectnickname = importlib.import_module("abc-ya-burnt")
from projectnickname.app import projectnickname

if __name__ == "__main__":
    projectnickname.run()