"""
{
  "account": {
    "id": "string",
    "type": "UNSPECIFIED",
    "cards": [
      {
        "id": "string",
        "pin": "string",
        "cvv": "string",
        "type": "UNSPECIFIED",
        "status": "UNSPECIFIED",
        "accountId": "string",
        "cardNumber": "string",
        "cardHolder": "string",
        "expiryDate": "2026-08-15",
        "paymentSystem": "UNSPECIFIED"
      }
    ],
    "status": "UNSPECIFIED",
    "balance": 0
  }
}
"""
import uuid
from pydantic import BaseModel, Field, ConfigDict, HttpUrl, EmailStr, ValidationError
from pydantic.alias_generators import to_camel
from datetime import date

class DocumentSchema(BaseModel):
    url: HttpUrl
    document: str

class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")

print(UserSchema(id="An", email="ANN@An.ru", lastName="MironoV", firstName="ANdreI", middleName="ANRyan", phoneNumber="1234555"))

try:
    tariff = DocumentSchema(
        url="localhost",
        document="document_data"
    )
except ValidationError as error:
    print(error)
    print(error.errors())
class CardScheme(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    id: str = "card-id"
    pin: str = "12345"
    cvv: str = "123"
    type: str
    status: str
    account_Id: str = Field(alias="accountId", default="account-id")
    card_number: str = Field(alias="cardNumber", default="1234567891012")
    card_holder: str = Field(alias="cardHolder")
    expiry_date: date = Field(alias="expiryDate")
    payment_system: str = Field(alias="paymentSystem")

#def get_uuid() -> str:
#   return str(uuid.uuid4())

class AccountSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    type: str = "CREDIT_CARD"
    cards: list[CardScheme] = Field(default_factory=list)
    status: str = "ACTIVE"
    balance: float = 25000

    def get_account_name(self) -> str:
        return f"{self.status}{self.type}"

account = AccountSchema()
account1 = AccountSchema()
account2 = AccountSchema()
print(account1)
print(account2)
print(account.get_account_name())

account_default_model = AccountSchema(
    id="account-id",
    type="CREDIT_CARD",
    cards=[
        CardScheme(
            id="card-id",
            pin="1234",
            cvv="123",
            type="PHYSICAL",
            status="Active",
            accountId="account-id",
            cardNumber="1234567891012",
            cardHolder="Mironov Andrew",
            expiryDate=date(2028,5,30),
            paymentSystem="MIR"
        )
    ],
    status='ACTIVE',
    balance=100.57
)
print('Account default model:', account_default_model)

account_dict = {
    "id": "account-id",
    "type": "CREDIT_CARD",
    "cards": [
        {
            "id": "card-id",
            "pin": "1234",
            "cvv": "123",
            "type": "PHYSICAL",
            "status": "Active",
            "accountId": "account-id",
            "cardNumber": "1234567891012",
            "cardHolder": "Mironov Andrey",
            "expiryDate": "2029-03-20",
            "paymentSystem": "MIR"
        }
    ],
    "status":"ACTIVE",
    "balance": 99.97
}

account_dict_model = AccountSchema(**account_dict)
print('Account dict model:', account_dict_model)
print(account_dict_model.model_dump(by_alias=True))

account_json = """{
    "id": "account-id",
    "type":"CREDIT_CARD",
    "cards":[
        {
            "id": "card-id",
            "pin": "1234",
            "cvv": "123",
            "type": "PHYSICAL",
            "status": "Active",
            "accountId": "account-id",
            "cardNumber": "1234567891012",
            "cardHolder": "Mironov Andrey",
            "expiryDate": "2029-03-20",
            "paymentSystem": "MIR"
        }
    ],
    "status":"ACTIVE",
    "balance": 199.97
    }
"""
account_json_model = AccountSchema.model_validate_json(account_json)
print("Account JSON model:", account_json_model)

#with open('account.json', 'r') as file:
#    account_data = file.read()
#AccountSchema.model_validate_json(account_data)