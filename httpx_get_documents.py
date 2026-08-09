import httpx
import time

create_user_payload = {
  "email": f"user.{time.time()}@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string",
  "phoneNumber": "string"
}

create_user_response = httpx.post ("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

print("Create user response: ", create_user_response_data)
print("status Code:", create_user_response.status_code)

open_credit_card_account_payload = {
    "userId": create_user_response_data["user"]["id"]
}

open_credit_card_account_response = httpx.post("http://localhost:8003/api/v1/accounts/open-credit-card-account", json=open_credit_card_account_payload)

open_credit_card_account_response_data = open_credit_card_account_response.json()
#print(open_credit_card_account_response_data)

get_tariff_document_response = httpx.get(
    f"http://localhost:8003/api/v1/documents/tariff-document/"
    f"{open_credit_card_account_response_data['account']['id']}"
)
get_tariff_document_response_data = get_tariff_document_response.json()
print(get_tariff_document_response_data)
print(get_tariff_document_response.status_code)

get_contract_document_response = httpx.get(
    f"http://localhost:8003/api/v1/documents/contract-document/"
    f"{open_credit_card_account_response_data['account']['id']}"
)
get_contract_document_response_data = get_contract_document_response.json()
print(get_contract_document_response_data)
print(get_contract_document_response.status_code)