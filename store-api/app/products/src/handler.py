import os
from datetime import datetime

from requests.status_codes import codes as http_code

__all__ = [
    'lambda_handle'
]

CWD = os.path.dirname(__file__)

log_prefix = '[products]'

def lambda_handle(event, context):
    """
    :param event: lambda event
    :type event: dict
    :param context: lambda context
    :type context: dict
    :return: void
    :rtype: None
    """
    try:
        start_time = datetime.now()
        print(log_prefix, 'START')

        print(log_prefix, 'some kind of product magic is happening!')

        duration = int((datetime.now() - start_time).total_seconds() * 1_000_000)

        print(log_prefix, 'COMPLETE')
        print(log_prefix, 'took', duration, 'microseconds')
        return http_code.ACCEPTED
    except Exception as error:
        print('%s error \n%s', log_prefix, error)
        return http_code.ERROR