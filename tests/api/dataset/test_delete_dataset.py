import pytest

@pytest.mark.anyio
class TestDeleteDataset:
    async def test_delete_then_404(self, async_client, auth_headers, create_dataset_in_db):
        ds = await create_dataset_in_db("to_delete", "desc", [])
        r_del = await async_client.delete(f"/datasets/{ds.id}", headers=auth_headers)
        assert r_del.status_code == 204, r_del.text

        r_get = await async_client.get(f"/datasets/{ds.id}", headers=auth_headers)
        assert r_get.status_code == 404
