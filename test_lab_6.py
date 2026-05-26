import pytest
from pydantic import ValidationError
from models import Person, Source, Block, Vote

# Тести для Person
def test_valid_person():
    p = Person(id=1, name="Victor Bulyk", addr="Kyiv")
    assert p.name == "Victor Bulyk"
def test_invalid_person_name():
    with pytest.raises(ValidationError):
        Person(id=1,name="Victor", addr="Kyiv")   
def test_invalid_person_id():
    with pytest.raises(ValidationError):
        Person(name="Victor", addr="Kyiv")    
    

def test_invalid_person_id():
    with pytest.raises(ValidationError):
        Person(id=-5, name="Ivan", addr="Kyiv")

# Тести для Source
def test_valid_source():
    s = Source(id=1, ip_addr="182.157.1.1", country_code="UA")
    assert s.country_code == "UA"

def test_invalid_source_country():
    with pytest.raises(ValidationError):
        Source(id=1, ip_addr="1.1.1.1", country_code="UKRAINE")

# Тести для Block
def test_valid_block():
    b = Block(id="a1b2c3d4", view=10, desc="test", img=b"data")
    assert b.view == 10

def test_invalid_block_id_format():
    with pytest.raises(ValidationError):
        Block(id="zzz", view=10, desc="test", img=b"data")

def test_negative_block_views():
    with pytest.raises(ValidationError):
        Block(id="abcdef12", view=-1, desc="test", img=b"data")

# Тести для Vote
def test_valid_vote():
    v = Vote(block_id="ffffffff", voter_id=1, timestamp="2023-10-10", source_id=2)
    assert v.voter_id == 1