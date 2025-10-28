#!/usr/bin/env python3
import threading
import time
from task_04_net import start_server, send_data

def main():
    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    time.sleep(1)  # give server a moment

    sample = {"name": "alice", "age": 30, "city": "paris"}
    send_data(sample)

    server_thread.join()

if __name__ == "__main__":
    main()
