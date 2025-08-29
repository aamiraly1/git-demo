def test_1():
    x=10
    y=20
    assert x==y
def test_2():
    name="Selenium"
    title="Selenium is a testing tool"
    assert name in title,"Name is different than title"
def test_login():
    print("Successfully logged in")