import pytest
import psycopg
from testcontainers.postgres import PostgresContainer


@pytest.fixture(scope="session")
def postgres_container():
    with PostgresContainer("postgres:latest") as postgres:
        yield postgres

def test_database_connection(postgres_container):

    conn = psycopg.connect(
        host=postgres_container.get_container_host_ip(),
        port=postgres_container.get_exposed_port(5432),
        user=postgres_container.username,
        password=postgres_container.password,
        dbname=postgres_container.dbname
    )

    cur = conn.cursor()
    cur.execute("SELECT 1")
    result = cur.fetchone()
    assert result[0] == 1
    cur.close()
    conn.close()