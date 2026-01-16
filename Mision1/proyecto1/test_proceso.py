from proceso import clean_id
def test_clean_id():
    assert clean_id("cc-75.087.345")=="75087345"
