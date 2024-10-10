
def my_cron_job():
    # your functionality goes here
    with open("/home/leorizaserver/applegenie/core_app_root/mycron.txt","a") as fileText:
        fileText.write("current cron job")
    fileText.close()
    print("end")