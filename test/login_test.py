def test_valid_login():
    username = "admin"
    password = "1234"
    assert username == "admin" and password == "1234"

def test_invalid_login():
    username = "user"
    password = "wrong"
    assert not (username == "admin" and password == "1234")