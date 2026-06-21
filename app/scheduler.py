import schedule
import time
import subprocess


def check_logs():
    try:
        # Open log file
        with open("app/logs/error.log", "r") as file:

            logs = file.read()

            # Check if log contains any errors
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

                # Add files to Git
                subprocess.run(
                    ["git", "add", "."]
                )

                # Create Git Commit
                subprocess.run(
                    [
                        "git",
                        "commit",
                        "-m",
                        "AI generated fix suggestion"
                    ]
                )

                print("\nGit Commit Created Successfully")

                # Push to GitHub
                print("\nPushing to GitHub...\n")

                subprocess.run(
                    [
                        "git",
                        "push",
                        "origin",
                        "ai-fix-branch"
                    ]
                )

                print("\nGitHub Push Completed")

                # Clear log file
                with open("app/logs/error.log", "w") as file:
                    file.write("")

                print("\nError log cleared")

            else:

                print("\nNo errors found in log file.")

    except FileNotFoundError:

        print("\nLog file not found.")

    except Exception as e:

        print("\nScheduler Error:")
        print(e)


# ====================================
# Run every 12 hours
# ====================================

schedule.every(12).hours.do(check_logs)

print("===================================")
print("Scheduler Started")
print("Checking logs every 12 hours...")
print("===================================")

# Run once immediately when scheduler starts
check_logs()

# Keep scheduler running forever
while True:
    schedule.run_pending()
    time.sleep(60)