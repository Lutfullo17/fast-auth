from pydantic import BaseModel
from typing import Optional

class SignUpSchemas(BaseModel):
    first_name: Optional[str]
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True
        Schema_extra = {
            'example':{
                'first_name': 'Nodir',
                'username': 'nodirjon',
                'email': 'nodir21@gmail.com',
                'password': 'password321'
            }
        }


class LoginSchemas(BaseModel):
    username: str
    password: str

class Settings(BaseModel):
    authjwt_secret_key: str = 'ddbe41871570a872d4c70fb9c4f6de94343d0ba81a04dbcb087407ce24fdfcee'