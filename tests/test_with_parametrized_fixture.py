# тест с параметризованной фикстурой
def test_param_fixture(fixture_with_params):
    print(fixture_with_params)
    assert fixture_with_params > 3
