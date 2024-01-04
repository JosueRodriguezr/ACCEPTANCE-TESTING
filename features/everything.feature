Feature: To-Do List Manager

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | Task          |
      | Buy groceries |
      | Pay bills     |
    When the user lists all tasks
    Then the output should contain:
      """
      Tasks:
      - Buy groceries
      - Pay bills
      """

  Scenario: Mark a task as completed
    Given the to-do list contains tasks:
      | Task          | Status   |
      | Buy groceries | Pending  |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | Task          |
      | Buy groceries |
      | Pay bills     |
    When the user clears the to-do list
    Then the to-do list should be empty
    
  # Add more specific details to the scenario titles and comments
  Scenario: Search for tasks by status
    Given the to-do list contains tasks:
      | Task          | Status   |
      | Buy groceries | Pending  |
      | Pay bills     | Completed|
    When the user searches for tasks with status "Pending"
    Then the output should contain:
      """
      Tasks with status "Pending":
      - Buy groceries
      """

  Scenario: Update task details
    Given the to-do list contains tasks:
      | Task          | Status   | Description          |
      | Buy groceries | Pending  | Remember to get milk.|
    When the user updates the details of task "Buy groceries" with status "In Progress" and a new description
    Then the to-do list should show updated details for task "Buy groceries"
      | Task          | Status      | Description                   |
      | Buy groceries | In Progress | New details for the task.     |
