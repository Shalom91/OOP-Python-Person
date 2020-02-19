import pytest
from person import Person

def test_hello():
    person1 = Person("Molash", 40, "male", "being rich, watching anime, and reading novels.")
    assert person1.hello() == "Hello, my name is Molash and I am 40 years old. My watching TV, and reading books."
