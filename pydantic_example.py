from pydantic import BaseModel

class Address(BaseModel):
    city: str
    zip_code: str
class User(BaseModel):
    id: int
    name: str
    email: str
    address: Address
    is_active: bool = False

user = User(id=1, name="AN", email="an@ex.ru", address={"city": "Moscow", "zip_code": "127206"})
print(user)
print(user.address.city)