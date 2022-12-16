import pytest


# change scope for cases
@pytest.fixture(scope='class')
def new_fix():
    variable = 'hi, there'
    print(variable)
    return variable


# ----only for autouse tests
# @pytest.fixture(autouse=True)
# def new_autouse_fix():
#     print('hi,there ^_^')


@pytest.fixture(scope='class')
def fixture_for_usefix():
    variable = 'meow meow meow'
    # print(variable)
    return variable


@pytest.fixture(params=[1, 2, 3, 4, 5])
def fixture_with_params(request):
    return request.param + 1


@pytest.fixture()
def fixture_addfinalize(request):
    print('this is before test')

    def teardown():
        print('this is after test')

    request.addfinalizer(teardown)


@pytest.fixture()
def fixture_yield():
    print('this is before test')
    yield
    print('this is after test')
