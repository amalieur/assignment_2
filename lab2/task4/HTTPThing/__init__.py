import json
import logging
import azure.functions as func
from integral import integral

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    integral_req = integral(0,3.14159)

    json_req = json.dumps(integral_req)

    return func.HttpResponse(json_req, mimetype='text/json') 