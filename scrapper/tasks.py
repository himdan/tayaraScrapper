import requests
import json
from typing import Any, List
from celery import Celery
from celery.schedules import crontab
from scrapper_common.producer import result_topic
import time

app = Celery('tasks', broker='pyamqp://guest:guest@broker//')

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=23, minute=56),
        scrap_tayara.s(),
    )




def _handle_search_result(_result: Any):
    print(_result)
    result_topic.send(_result)

def _handle_search_results(_results: List[Any], record_count: int)->int:
    for k,result in enumerate(_results):
        _handle_search_result(result)
        record_count += 1
    return record_count



@app.task
def scrap_tayara():
    url = 'https://www.tayara.tn/api/marketplace/search-api/'
    headers = {
        'authority': 'www.tayara.tn',
        'accept': 'application/json',
        'content-type': 'application/json',
        'origin': 'https://www.tayara.tn',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'

    }
    _next_page = True
    _current_page = 0
    _record_count = 0
    _limit = 30
    _backOff = 0
    _backOffTime = 30

    while _next_page:
        data = {"searchRequest": {"query": "", "offset": _current_page * _limit, "limit": _limit, "sort": 0,
                                  "filter": {"categoryId": "60be84bc50ab95b45b08a093", "subCategoryId": "",
                                             "adParamsMap": {}, "rangeAdParamsMap": {}, "governorate": "",
                                             "delegation": [""], "minPrice": 0, "maxPrice": 0, "productTypeList": [],
                                             "level": 0, "state": 2}}, "withPremium": True}
        response = requests.post(url, data=json.dumps(data).encode('utf-8'), headers=headers)
        if response.status_code == 200:
            container = json.loads(response.content)
            total_records = container[0][1] if container[0][1] else 0
            results = container[0][0]
            print('-----------------------------------')
            _record_count = _handle_search_results(_results=results, record_count=_record_count)
            print('-----------------------------------')
            _next_page = _record_count < total_records
            _current_page += 1
            _backOff = 0
            continue
        print('-----await For Response--------')
        _backOff += 1
        time.sleep(_backOff * _backOffTime)




