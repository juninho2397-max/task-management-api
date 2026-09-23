from fastapi.testclient import TestClient

from aplicativo.main import aplicativo


client = TestClient(aplicativo)


def test_create_and_list_task():
    create_response = client.post(
        "/tarefas",
        json={"titulo": "Test automated task"},
    )

    assert create_response.status_code == 201

    created_task = create_response.json()

    assert created_task["titulo"] == "Test automated task"
    assert "id" in created_task

    list_response = client.get("/tarefas")

    assert list_response.status_code == 200

    tasks = list_response.json()

    assert any(
        task["id"] == created_task["id"]
        for task in tasks
    )
