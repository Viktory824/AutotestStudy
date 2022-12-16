import pytest


@pytest.mark.usefixtures('fixture_for_usefix')
def test_usefix():
    # print(f'i got fixture - {fixture_for_usefix}')
    assert 1 == 1


@pytest.mark.dev
def test_marks():
    print(f'meow - ^_^')
    assert 1 == 1


@pytest.mark.dev
def test_marks_new():
    print(f'meow - ^_^')
    assert 1 == 1


@pytest.mark.parametrize('param_name', [1, 2, 3, 100, 5, 7, -10])
def test_with_params(param_name):
    assert param_name > 0, 'Заданный параметр меньше нуля'
