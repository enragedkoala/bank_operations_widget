import pytest
from src.decorators import log
from src.masks import get_mask


def test_log_file_with_get_mask_corr():
    log_params = log(filename="testing_log")(get_mask)
    func_params = log_params("1234122412341234")
    with open("testing_log", "r") as file:
        assert file.read() == "get_mask ok.\n"


def test_log_file_with_get_mask_value_error():
    with pytest.raises(ValueError):
        log_params = log(filename="testing_log")(get_mask)
        func_params = log_params("123412241234234")
    with open("testing_log", "r") as file:
        assert file.read() == "get_mask error: ValueError. Inputs: ('123412241234234',), {}\n"


def test_log_file_with_get_mask_type_error():
    with pytest.raises(TypeError):
        log_params = log(filename="testing_log")(get_mask)
        func_params = log_params("12341224hh1234234")
    with open("testing_log", "r") as file:
        assert file.read() == "get_mask error: TypeError. Inputs: ('12341224hh1234234',), {}\n"


def test_log_no_file_with_get_mask_corr(capsys):
    log_params = log()(get_mask)
    func_params = log_params("1234122412341234")
    captured = capsys.readouterr()
    assert captured.out.strip() == "get_mask ok."


def test_log_no_file_with_get_mask_value_error(capsys):
    with pytest.raises(ValueError):
        log_params = log()(get_mask)
        func_params = log_params("123412241234234")
    captured = capsys.readouterr()
    assert (captured.out.strip() == "get_mask error: ValueError. Inputs: ('123412241234234',), {}")


def test_log_no_file_with_get_mask_type_error(capsys):
    with pytest.raises(TypeError):
        log_params = log()(get_mask)
        func_params = log_params("aa123412241234234")
    captured = capsys.readouterr()
    assert captured.out.strip() == "get_mask error: TypeError. Inputs: ('aa123412241234234',), {}"
