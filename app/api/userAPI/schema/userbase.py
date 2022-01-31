from pydantic import EmailStr,BaseModel

class User(BaseModel):
    """
        - # first name of the Person
        - last name of the Person
        - username of the Person
        - gender of the Person
    """
    first_name:str
    last_name:str
    username:str
    sex:str = "Male"
    email:EmailStr