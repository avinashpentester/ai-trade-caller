# utils/scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import datetime
import pytz

def start_scheduler(job_func, interval_minutes):
    scheduler = BackgroundScheduler(timezone=pytz.timezone("Asia/Kolkata"))
    scheduler.add_job(job_func, IntervalTrigger(minutes=interval_minutes))
    scheduler.start()
    print("⏱ Scheduler started...")