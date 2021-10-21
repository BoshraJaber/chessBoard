from numpy2 import __version__
from numpy2 import chessBoard


def test_version():
    assert __version__ == '0.1.0'

def test_same_row():
    new_chess=chessBoard()
    new_chess.add_red(2,6)
    new_chess.add_blue(2,2)
    assert new_chess.is_under_attack() == True

