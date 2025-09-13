from modules.ui.input_service import InputService


def test_say_hello():
    say_hello = InputService()
    assert say_hello.say_hello() == "Hello World"
