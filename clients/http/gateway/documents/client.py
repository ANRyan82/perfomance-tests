from typing import TypedDict

from httpx import Response, QueryParams

from clients.http.client import HTTPClient


class DocumentGatewayHTTPClient(HTTPClient):
    def get_tariff_document_api(self, account_id: str) -> Response:
        return self.get(f"/api/v1/documents/tariff-document/{account_id}")
    def get_contract_document_api(self, account_id: str) -> Response:
        return self.get(f"/api/v1/documents/contract-document/{account_id}")