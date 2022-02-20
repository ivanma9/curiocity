import schedule
import time
def show_name():
    print("squirtle squad")

schedule.every(4).seconds.do(show_name)

while 1:
    schedule.run_pending()
    # time.sleep(1)