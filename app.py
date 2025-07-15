from flask import Flask

app = Flask(__name__)
rt = app.route


def TaskForm():
    return "TaskForm"


def TaskList():
    return "TaskList"


def Layout(TaskForm, TaskList, ui_state: dict):
    assert TaskForm.__name__ == "TaskForm"
    assert TaskList.__name__ == "TaskList"
    return f"""
             <p id='tasklist'>{TaskList() if ui_state[TaskList]['active'] else None}</p>
             <p id='taskform'>{TaskForm() if ui_state[TaskForm]['active'] else None}</p> 
             {ui_state}
            """


@rt("/")
def index():
    return Layout(
        TaskForm, TaskList, {TaskList: {"active": False}, TaskForm: {"active": True}}
    )


if __name__ == "__main__":
    app.run(port=5000, debug=True)
