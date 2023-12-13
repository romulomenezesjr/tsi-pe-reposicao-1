import mock
import builtins
import main


def test_q1(capfd):
    input_output = {
        '7': 'O número não possui divisores multiplos de 3\n',
        '3': 'Quantidade de divisores divisiveis por 3: 1\n',
        '555':'Quantidade de divisores divisiveis por 3: 4\n',
        '3144':'Quantidade de divisores divisiveis por 3: 8\n',
        '17640':'Quantidade de divisores divisiveis por 3: 48\n'
    }
    for k, v in input_output.items():
        with mock.patch.object(builtins, 'input', lambda _: k):
            main.q1()
            out, err = capfd.readouterr()
            assert out == v

def test_q2(capfd, monkeypatch):
    input_output = {
        '1,3': '6\n',
        '-2,2': '3\n',
        '10,-10': '55\n',
    }
    for k,v in input_output.items():
        monkeypatch.setitem(__builtins__, 'input', make_multiple_inputs(k.split(',')))
        main.q2()
        out, _ = capfd.readouterr()
        assert out == v


def make_multiple_inputs(inputs):
    """ provides a function to call for every input requested. """
    def next_input(_):
        """ provides the first item in the list. """
        return inputs.pop()
    return next_input

def test_q3(capfd, monkeypatch):
    input_output = {
        '1000,500,10,5': 'O custo total mensal estimado para a infraestrutura é de R$ 3600.00.\n',
        '10000,1000,50,10': 'O custo total mensal está acima do limite.\n',
    }
    for k,v in input_output.items():
        monkeypatch.setitem(__builtins__, 'input', make_multiple_inputs(k.split(',')))
        main.q3()
        out, _ = capfd.readouterr()
        assert out == v


def test_q4(capfd):
    input_output = {
        '0': '0.0\n',
        '8': '1/3 + 2/6 + 3/9 + 4/12 + 5/15 + 6/18 + 7/21 + 8/24\n2.67\n',
        '4': '1/3 + 2/6 + 3/9 + 4/12\n1.33\n',
    }
    for k, v in input_output.items():
        with mock.patch.object(builtins, 'input', lambda _: k):
            main.q4()
            out, err = capfd.readouterr()
            assert out == v