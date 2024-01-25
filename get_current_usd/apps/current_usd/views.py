from decimal import Decimal
from http import HTTPStatus
from json import loads
import requests

from django.core.cache import cache
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET'])
def get_current_usd(request):
    current_usd = cache.get(settings.CURRENT_USD_CACHED_NAME)
    if current_usd:
        json_response = current_usd
    else:
        response = requests.get(settings.CURRENCY_API_URL)
        if response.status_code != 200:
            return JsonResponse(
                settings.SERVICE_UNAVAILABLE_MESSAGE,
                status=HTTPStatus.SERVICE_UNAVAILABLE,
            )
        json_content = loads(response.content)
        json_response = {"current_usd": {}, "last_responses": []}
        json_response["current_usd"]["date"] = json_content["date"]
        json_response["current_usd"]["timestamp"] = json_content["timestamp"]
        json_response["current_usd"]["base"] = "USD"
        json_response["current_usd"]["rates"] = {
            "RUB": round(Decimal(1) / Decimal(json_content["rates"]["USD"]), 8)
        }

    # Добавление последних запросов
    last_responses = cache.get(settings.LAST_RESPONSES_CACHED_NAME) or []
    for request in last_responses[::-1]:
        if len(last_responses) >= settings.LAST_RESPONSES_COUNT:
            last_responses.pop(0)
        json_response["last_responses"].append(request)
    last_responses.append(json_response["current_usd"])
    cache.set(
        settings.LAST_RESPONSES_CACHED_NAME,
        last_responses,
        settings.LAST_RESPONSES_TIMEOUT,
    )

    return JsonResponse(json_response)
