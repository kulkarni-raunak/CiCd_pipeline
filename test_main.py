# test_main.py

from main import main
import sys
from io import StringIO

def test_main():
    saved_stdout = sys.stdout
    try:
        out = StringIO()
        sys.stdout = out
        main()
        output = out.getvalue().strip()
        assert output == "Hello, World!"
    finally:
        sys.stdout = saved_stdout
