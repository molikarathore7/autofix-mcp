import schedule
import time


def check_logs():
    try:
        with open("app/logs/error.log", "r") as file:

            logs = file.read()

            if logs.strip():

                print("\nERROR FOUND IN LOG FILE")
                print("--------------------------------")
                print(logs)
                print("--------------------------------")

            else:

                print("\nNo errors found in log file.")

    except FileNotFoundError:

        print("\nLog file not found.")

    except Exception as e:

        print("\nFailed to read log file:", e)


# Run every 20 seconds
schedule.every(20).seconds.do(check_logs)

print("Scheduler Started...")
print("Checking logs every 20 seconds...")

# Run once immediately when the scheduler starts
check_logs()

# Keep scheduler running
while True:
    schedule.run_pending()
    time.sleep(1)