from src.frida import *

def test_frida_wheek():
    assert wheek() == "wheek!"

def test_frida_eat():
    assert eat() == "Frida is eating"