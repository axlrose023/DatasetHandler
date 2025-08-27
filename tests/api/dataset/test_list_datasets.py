import pytest

@pytest.mark.anyio
class TestListDatasets:
    async def test_list_empty(self, async_client, auth_headers):
        r = await async_client.get("/datasets/", headers=auth_headers)
        assert r.status_code == 200
        assert r.json() == []

    async def test_list_with_counts(self, async_client, auth_headers, create_dataset_in_db, items_payloads):
        await create_dataset_in_db("list_ds1", "no items", [])
        await create_dataset_in_db("list_ds2", "with items", items_payloads)
        r = await async_client.get("/datasets/", headers=auth_headers)
        assert r.status_code == 200
        data = r.json()
        assert len(data) == 2
        by_name = {d["name"]: d for d in data}
        assert by_name["list_ds1"]["count"] == 0
        assert by_name["list_ds2"]["count"] == 3
