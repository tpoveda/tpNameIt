import pytest

from tpDcc.tools.nameit import __version__


def test_version():
    assert __version__.__version__