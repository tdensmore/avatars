import pytest
from testcontainers.postgres import PostgresContainer
import psycopg2

@pytest.fixture(scope="session")
def postgres_container():
    with PostgresContainer() as postgres:
        yield postgres

def test_database_connection(postgres_container):
    conn = psycopg2.connect(
        dbname=postgres_container.get_container_host_port().split("/")[1],
        user="postgres",
        password="password",
        host=postgres_container.get_container_host_port().split(":")[0],
        port=postgres_container.get_container_host_port().split(":")[1].split("/")[0]
    )
    cur = conn.cursor()
    cur.execute("SELECT 1")
    result = cur.fetchone()
    assert result[0] == 1
    cur.close()
    conn.close()