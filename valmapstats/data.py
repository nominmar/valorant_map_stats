import requests
import json
from collections import namedtuple
from urllib.parse import urlencode, urlunparse

from config import MATCH_ENDPOINT


class PuuidException(Exception):
    pass


def get_url(game_mode: str, game_map: str, game_region: str, puuid: str):
    """
    Create url for a given endpoint & user options
    :param game_mode: valorant game mode
    :param game_map: valorant map
    :param game_region: game region
    :param puuid: player unique id
    :return: constructed url
    """
    Components = namedtuple(
        typename='Components',
        field_names=['scheme', 'netloc', 'path',  'params', 'query', 'fragment'])

    url_path = "/".join([MATCH_ENDPOINT, game_region, puuid])
    url = urlunparse(
        Components(
            scheme='https',
            netloc="api.henrikdev.xyz",
            path=url_path,
            params='',
            query=urlencode({'mode': game_mode,
                             'map': game_map}),
            fragment=''
        )
    )
    return url


def get_request(game_mode: str, game_map: str, game_region: str, puuid: str) -> dict:
    """
    Send get request to henrik api: https://github.com/Henrik-3/unofficial-valorant-api
    :raises PuuidException: in case puuid is wrong
    :return: reponse dictionary
    """
    url = get_url(**inputs)
    header = {"accept": "application/json"}
    try:
        response = requests.get(url, headers=header)
        if response.status_code == 400:
            raise PuuidException("Wrong puuid")
        return response.json()
    except requests.exceptions.ConnectionError as err:
        raise
