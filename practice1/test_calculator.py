import practice1.calculator as calculator

def test_increment():
    # given (expected result)
    expected_result = 5
    # when (acutal result)
    actual_result = calculator.increment(4)
    # then (expected == actual)
    assert expected_result == actual_result

def test_stub_increment(mocker):
    # given (prepairing, expected)
    mocker.patch('calculator.increment', return_value=30)

    # when
    actual_result = calculator.increment(4)

    # then
    assert 30 == actual_result

def test_stub_mock_increment(mocker):
    # given (prepairing, expected)
    mocked_increment = mocker.patch('calculator.increment', return_value=30)

    # when
    actual_result = calculator.increment(4)

    # then
    assert 30 == actual_result

    # mocking
    mocked_increment.assert_called()
    assert mocked_increment.call_count == 1
    assert mocked_increment.call_args == mocker.call(4)
    assert mocked_increment.call_args_list == [mocker.call(4)]

def test_decrement():
    # given
    expected_result = 5
    # when
    actual_result = calculator.decrement(6)
    # then
    assert expected_result == actual_result

def test_stub_decrement(mocker):
    # given (prepairing, expected)
    mocker.patch('calculator.decrement', return_value=30)

    # when
    actual_result = calculator.decrement(6)

    # then
    assert 30 == actual_result

def test_stub_mock_decrement(mocker):
    # given (prepairing, expected)
    mocked_decrement = mocker.patch('calculator.decrement', return_value=30)

    # when
    actual_result = calculator.decrement(6)

    # then
    assert 30 == actual_result

    # mocking
    mocked_decrement.assert_called()
    assert mocked_decrement.call_count == 1
    assert mocked_decrement.call_args == mocker.call(6)
    assert mocked_decrement.call_args_list == [mocker.call(6)]