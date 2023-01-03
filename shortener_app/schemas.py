from pydantic import BaseModel

class URLBase(BaseModel):
    target_url : str

class URL(URLBase):
    is_active : bool
    clicks : int #count for how many times the shortened url vistied.

    class Config:
        orm_mode = True

class URLInfo(URL):
    url: str
    admin_url : str