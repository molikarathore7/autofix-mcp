import schedule
import time
import subprocess


def check_logs():
    try:
        # Open error log file
        with open("app/logs/error.log", "r") as file:

            logs = file.read()

            # If log file contains errors
            if logs.strip():

                print("\n===================================")
                print("ERROR FOUND IN LOG FILE")
                print("===================================")

                print(logs)

                print("\nRunning AI Fixer...\n")

                # Run Gemini Fixer
                subprocess.run(
                    ["python", "ai/fixer.py"]
                )

                print("\nCreating Git Commit...\n")

                # Add changed files
                subprocess.run(
                    ["git", "add", "."]
                )

                # Create commit
                subprocess.run(
                    [
                        "git",
                        "commit",
                        "-m",
                        "AI generated fix suggestion"
                    ]
                )

                print("\nGit Commit Created Successfully")

            else:

                print("\nNo errors found in log file.")

    except FileNotFoundError:

        print("\nLog file not found.")

    except Exception as e:

        print("\nScheduler Error:")
        print(e)


# Run every 20 seconds
schedule.every(20).seconds.do(check_logs)

print("===================================")
print("Scheduler Started")
print("Checking logs every 20 seconds...")
print("===================================")

# Run immediately once
check_logs()

# Keep scheduler running forever
while True:
    schedule.run_pending()
    time.sleep(1)