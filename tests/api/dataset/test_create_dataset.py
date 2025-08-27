import pytest

@pytest.mark.anyio
class TestCreateDataset:
    async def test_create_201(self, async_client, auth_headers, dataset_payload):
        r = await async_client.post("/datasets/", json=dataset_payload, headers=auth_headers)
        assert r.status_code == 201, r.text
        body = r.json()
        assert body["id"] > 0
        assert body["name"] == dataset_payload["name"]
        assert body["description"] == dataset_payload["description"]
        assert body["count"] == 0

    async def test_create_duplicate(self, async_client, auth_headers, dataset_payload):
        r1 = await async_client.post("/datasets/", json=dataset_payload, headers=auth_headers)
        assert r1.status_code == 201, r1.text
        r2 = await async_client.post("/datasets/", json=dataset_payload, headers=auth_headers)
        assert r2.status_code in (400, 409), r2.text
