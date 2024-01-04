from behave import given, when, then
from main import ToDoListManager

@given("the to-do list is empty")
def step_empty_todo_list(world):
    world.todo_manager = ToDoListManager()

@when('the user adds a task "{task}"')
def step_add_task(world, task):
    world.todo_manager.add_task(task)

@then('the to-do list should contain "{task}"')
def step_check_task_in_list(world, task):
    assert any(task_obj.name == task for task_obj in world.todo_manager.tasks)

@given('the to-do list contains tasks:')
def step_given_task_list(world):
    world.todo_manager = ToDoListManager()
    for row in world.table:
        world.todo_manager.add_task(row['Task'])

@when("the user lists all tasks")
def step_list_all_tasks(world):
    world.task_list = world.todo_manager.list_tasks()

@then("the output should contain:")
def step_check_task_output(world):
    expected_output = world.text.strip()
    actual_output = "\n".join(world.task_list)
    assert actual_output == expected_output

@when('the user marks task "{task}" as completed')
def step_mark_task_completed(world, task):
    world.todo_manager.mark_task_completed(task)

@then('the to-do list should show task "{task}" as completed')
def step_check_task_completed(world, task):
    for t in world.todo_manager.tasks:
        if t.name == task:
            assert t.status == "Completed"

@when("the user clears the to-do list")
def step_clear_todo_list(world):
    world.todo_manager.clear_all_tasks()

@then("the to-do list should be empty")
def step_check_empty_todo_list(world):
    assert not world.todo_manager.tasks

@when('the user searches for tasks with status "{status}"')
def step_search_tasks_by_status(world, status):
    world.searched_tasks = world.todo_manager.search_tasks_by_status(status)

@then('the searched output should contain:')
def step_check_searched_tasks_output(world):
    expected_output = world.text.strip()
    actual_output = "\n".join(task.name for task in world.searched_tasks)
    assert actual_output == expected_output

@when('the user updates the details of task "{task}" with status "{status}" and a new description')
def step_update_task_details(world, task, status):
    for t in world.todo_manager.tasks:
        if t.name == task:
            t.status = status
            t.description = "New details for the task."
            return

@then('the to-do list should show updated details for task "{task}"')
def step_check_updated_task_details(world, task):
    for t in world.todo_manager.tasks:
        if t.name == task:
            assert t.status == "In Progress"
            assert t.description == "New details for the task."

@given(u'the to-do list contains tasks')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the to-do list contains tasks')


@then(u'the output should contain')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the output should contain')