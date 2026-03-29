# system_info_reporter/main.py

import time
from datetime import datetime
from system_info_reporter import get_system_info


def display(data):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\n------ SYSTEM INFO REPORT ------")
    print(f"Time: {current_time}\n")

    print(f"CPU Usage: {data['cpu']}%")

    print(f"Memory Usage: {data['memory'][0]} GB / {data['memory'][1]} GB ({data['memory'][2]}%)")

    print(f"Disk Usage: {data['disk'][0]} GB / {data['disk'][1]} GB ({data['disk'][2]}%)")

    print("--------------------------------")


def main():
    print("System Info Reporter Started ")

    try:
        while True:
            data = get_system_info()
            display(data)
            time.sleep(3)

    except KeyboardInterrupt:
        print("\nProgram stopped gracefully ")


if __name__ == "__main__":
    main()