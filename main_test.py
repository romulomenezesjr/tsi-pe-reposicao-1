import mock
import builtins
import main

def make_multiple_inputs(inputs):
    """ provides a function to call for every input requested. """
    def next_input(_):
        """ provides the first item in the list. """
        return inputs.pop()
    return next_input

def test_q1(capfd, monkeypatch):
    input_output = {
        '555,777,666': '555\n666\n777\n',
        '3,2,1': '1\n2\n3\n',
        '2,3,2': '2\n2\n3\n',
    }
    for k,v in input_output.items():
        monkeypatch.setitem(__builtins__, 'input', make_multiple_inputs(k.split(',')))
        main.q1()
        out, _ = capfd.readouterr()
        assert out == v

def test_q2(capfd, monkeypatch):
    input_output = {
        '80,1': '90.00\n',
        '301,3': '282.00\n',
        '300,3': '270.00\n',
        '1320,10': '4740.00\n',
    }
    for k,v in input_output.items():
        monkeypatch.setitem(__builtins__, 'input', make_multiple_inputs(k.split(',')))
        main.q2()
        out, _ = capfd.readouterr()
        assert out == v

def test_q3(capfd):
    input_output = {
        '1': '1\n',
        '2': '1\n2\n',
        '5': '1\n1 2\n1 2 3\n1 2 3 4\n1 2 3 4 5\n',
        '10': '1\n1 2\n1 2 3\n1 2 3 4\n1 2 3 4 5\n1 2 3 4 5 6\n1 2 3 4 5 6 7\n1 2 3 4 5 6 7 8\n1 2 3 4 5 6 7 8 9\n1 2 3 4 5 6 7 8 9 10\n'
    }
    for k, v in input_output.items():
        with mock.patch.object(builtins, 'input', lambda _: k):
            main.q1()
            out, err = capfd.readouterr()
            assert out == v

