from proceso import clean_id 
from proceso import merge_name

def test_clean_id():
    assert clean_id("cc-75.087.345")=="75087345"

def test_merge_name():
    assert merge_name("Ana", "Rodriguez")=="Ana Rodriguez"   

