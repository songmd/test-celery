from __future__ import absolute_import, unicode_literals

from testcelery.celery import app as celery_app

import logging

logger = logging.getLogger('celery.tasks')
logger.info('hello test2')


@celery_app.task
def test():
    logger.info('hello test')
    print('hello test')


print(test.name)

celery_app.conf.beat_schedule = {
    'add-every-5-seconds': {
        'task': 'testap.tasks.test',
        'schedule': 5.0,
    },
}
