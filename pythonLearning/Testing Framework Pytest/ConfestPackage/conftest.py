import pytest

@pytest.fixture(scope="module")
def set():
    print("a SET")
    print("B set")
    yield
    print("c Set")
    print("d set")


@pytest.fixture(scope="module")
def moduleSetUp():
    print("a module set")
    print("b module set")
    yield
    print("c module set")
    print("d module set")

