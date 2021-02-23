import pytest
import requests


def test_movie_summer():
    param = {'q': 'Summer'}
    response = requests.get("http://localhost:3000/api/v1/suggestions", params=param)
    json_response = response.json()
    print(json_response)
    print(response.status_code)
    content_type = response.headers['Content-Type']
    print(content_type)
    assert content_type == "application/json; charset=utf-8"
    arr_len = len(json_response)
    assert arr_len == 1


def test_movie_of():
    param = {'q': 'of'}
    response = requests.get("http://localhost:3000/api/v1/suggestions", params=param)
    json_response1 = response.json()
    print(json_response1)
    print(response.status_code)
    content_type = response.headers['Content-Type']
    assert content_type == "application/json; charset=utf-8"
    arr_len1 = len(json_response1)
    assert arr_len1 == 7
    print(json_response1[0])
    print(json_response1[1])
    print(json_response1[2])


def test_movie_of_rotten():
    param = {'q': 'of', 'sortBy':'rotten_tomatoes'}
    response = requests.get("http://localhost:3000/api/v1/suggestions", params=param)
    json_response2 = response.json()
    print(json_response2)
    print(response.status_code)
    content_type = response.headers['Content-Type']
    assert content_type == "application/json; charset=utf-8"
    arr_len2 = len(json_response2)
    assert arr_len2 == 7
    print(json_response2[0])
    print(json_response2[1])
    print(json_response2[2])


def test_movie_of_audience():
    param = {'q': 'of', 'sortBy':'audience_score'}
    response = requests.get("http://localhost:3000/api/v1/suggestions", params=param)
    json_response3 = response.json()
    print(json_response3)
    print(response.status_code)
    content_type = response.headers['Content-Type']
    assert content_type == "application/json; charset=utf-8"
    arr_len3 = len(json_response3)
    assert arr_len3 == 7
    print(json_response3[0])
    print(json_response3[1])
    print(json_response3[2])


def test_movie_of_some_other_key():
    param = {'q': 'of', 'sortBy':'some_other_key'}
    response = requests.get("http://localhost:3000/api/v1/suggestions", params=param)
    STATUS_CODE = response.status_code
    assert STATUS_CODE == 400


def test_movie_no_param():
    param = {}
    response = requests.get("http://localhost:3000/api/v1/suggestions", params=param)
    STATUS_CODE = response.status_code
    assert STATUS_CODE == 400