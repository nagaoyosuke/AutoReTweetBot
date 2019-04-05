from apscheduler.schedulers.blocking import BlockingScheduler
import serch

twische = BlockingScheduler()

@twische.scheduled_job('interval',minutes=360)
def timed_job():
    serch.update()

if __name__ == "__main__":
    twische.start()