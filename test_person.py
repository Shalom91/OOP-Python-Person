import pytest
from person import Person

def test_hello():
    person1 = Person("Molash", 40, "male", "being rich, watching anime, and reading novels.")
    assert Person.hello(person1) == "Hello, my name is Molash and I am 40 years old. My interests are being rich, watching anime, and reading novels."