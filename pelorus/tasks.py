from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery import shared_task
from celery.utils.log import get_task_logger
 
logger = get_task_logger(__name__)

@shared_task
def test_celery_worker():
    print("Celery Workers are working fine.")
 
# A periodic task that will run every minute (the symbol "*" means every)
@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")))
def task_example():
    logger.info("Task started")
    # add code
    logger.info("Task finished")