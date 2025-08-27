import pytest

@pytest.mark.anyio
class TestGetDatasetById:
    async def test_ok(self, async_client, auth_headers, create_dataset_in_db, items_payloads):
        ds = await create_dataset_in_db("by_id_ds", "desc", items_payloads[:2])
        r = await async_client.get(f"/datasets/{ds.id}", headers=auth_headers)
        assert r.status_code == 200, r.text
        body = r.json()
        assert body["id"] == ds.id
        assert body["name"] == "by_id_ds"
        assert body["count"] == 2

    async def test_404(self, async_client, auth_headers):
        r = await async_client.get("/datasets/999999", headers=auth_headers)
        assert r.status_code == 404
