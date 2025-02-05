import pytest
from predictable_jokes.jokes import tell_joke

def test_tell_joke():
    assert isinstance(tell_joke(), str)
    assert isinstance(tell_joke(topic="bayes"), str)
    assert isinstance(tell_joke(complexity="easy"), str)

if __name__ == "__main__":
    pytest.main()
