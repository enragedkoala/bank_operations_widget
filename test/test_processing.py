from src.processing import filter_by_state, sort_by_date
import pytest


def test_filter_by_state_correct(list_for_processing):
    assert filter_by_state(list_for_processing) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    assert filter_by_state(list_for_processing, "CANCELED") == [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def test_filter_by_state_wrong_data_type():
    assert filter_by_state("dfdfd") == []
    assert filter_by_state(123123) == []
    assert filter_by_state({1: 2}) == []
    assert filter_by_state(12312.0) == []


def test_filter_by_state_no_state():
    assert filter_by_state([{'id': 41428829, 'date': '2019-07-03T18:35:29.512364'}]) == []
    assert filter_by_state([]) == []


def test_sort_by_date_correct(list_for_processing):
    assert sort_by_date(list_for_processing) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    assert sort_by_date(list_for_processing, descending= False) == [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]


def test_sort_by_date_wrong_data_type():
    assert sort_by_date(123) == []
    assert sort_by_date("123") == []
    assert sort_by_date({1: 23}) == []
    assert sort_by_date(12.3) == []


def test_sort_by_date_no_date():
    assert sort_by_date([{'id': 41428829, 'state': 'EXECUTED'},
                         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}]) == []
    assert sort_by_date([]) == []