import pytest
from httpx import AsyncClient

auth_prefix = f"/api/v1/auth"

@pytest.mark.asyncio
async def test_user_creation(client):
    response = await client.get(url="/dev")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


@pytest.mark.asyncio
async def test_abc(client):
    assert 1 == 1


@pytest.mark.asyncio
async def test_get_all_posts(client: AsyncClient):
    response = await client.get("/posts")
    assert response.status_code == 200
    assert len(response.json()) == 0