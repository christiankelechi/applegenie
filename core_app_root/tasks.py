# myapp/tasks.py
from background_task import background

@background(schedule=10)  # Schedule to run every 60 seconds
def my_cron_job():
    with open("core_app_root/mycron.txt", "a") as fileText:
        fileText.write("current cron job 1")
    print("end")


my_cron_job(repeat=60)  # Repeat every 60 seconds
