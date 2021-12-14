import json
import logging
from service.scraping_service import (scraping_twitter)

logger = logging.getLogger()


def scraping_handler(event, context):
    logger.warning(context)
    tw_list = scraping_twitter(event)
    response = {
        "statusCode": 200,
        "body": json.dumps(tw_list)
    }

    return response

# def import_findings_handler(event, context):
#     try:
#         logger.warning(event)
#         return code_finding(event)
#     except Exception as error:
#         logger.setLevel(logging.ERROR)
#         logger.error("Error {}".format(error))
#         raise
#
#
