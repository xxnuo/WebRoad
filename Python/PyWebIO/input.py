from pywebio import *

def main():  # PyWebIO application function
    output.put_text("hello")

start_server(main, port=8086, debug=True, remote_access=True)