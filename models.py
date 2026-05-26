import sqlite3
from pydantic import BaseModel, Field
from typing import List

conn = sqlite3.connect("blockprocessor.db", check_same_thread=False)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

class Person(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(pattern= r"^[A-Za-z]+\ [A-Za-z]+$")
    addr: str

    @staticmethod
    def select_all() -> List["Person"]:
        rows = cur.execute("SELECT * FROM PERSONS").fetchall()
        return [Person(**dict(row)) for row in rows]

class Source(BaseModel):
    id: int = Field(gt=0)
    ip_addr: str  
    country_code: str = Field(min_length=2, max_length=2, pattern=r"^[A-Z]{2}$")

    @staticmethod
    def select_all() -> List["Source"]:
        rows = cur.execute("SELECT * FROM SOURCES").fetchall()
        return [Source(**dict(row)) for row in rows]    #row_dict = dict(row)
                                                        #Source(id=row_dict['id'], ip_addr=row_dict['ip_addr'], country_code=row_dict['country_code'])

class Block(BaseModel):
    id: str = Field(pattern=r"^[0-9a-fA-F]{8}$")
    view: int = Field(ge=0)
    desc: str
    img: bytes

    @staticmethod
    def select_all() -> List["Block"]:
        rows = cur.execute("SELECT * FROM BLOCKS").fetchall()
        return [Block(**dict(row)) for row in rows]  
class Vote(BaseModel):
    block_id: str = Field(pattern=r"^[0-9a-fA-F]{8}$")
    voter_id: int = Field(gt=0)
    timestamp: str  
    source_id: int = Field(gt=0)

    @staticmethod
    def select_all() -> List["Vote"]:
        rows = cur.execute("SELECT * FROM VOTES").fetchall()
        return [Vote(**dict(row)) for row in rows]
 
