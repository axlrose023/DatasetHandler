import pytest

@pytest.mark.anyio
class TestGetDatasetByName:
    async def test_ok(self, async_client, auth_headers, create_dataset_in_db, items_payloads):
        ds = await create_dataset_in_db("by_name_ds", "desc", items_payloads)
        r = await async_client.get(f"/datasets/name/{ds.name}", headers=auth_headers)
        assert r.status_code == 200, r.text
        body = r.json()
        assert body["id"] == ds.id
        assert body["name"] == "by_name_ds"
        assert body["count"] == 3

    async def test_404(self, async_client, auth_headers):
        r = await async_client.get("/datasets/name/not_exists", headers=auth_headers)
        assert r.status_code == 404
