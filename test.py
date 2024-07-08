from lib.PyDownThread import PyDownThread

downloader = PyDownThread([
    "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/242px-Python-logo-notext.svg.png",
], output="./images")
downloader.start()