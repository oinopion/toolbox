import pytest
from toolbox.models import Story, Task, Project


class TestProjectCreation:
    def test_basic_creation(self):
        title = "Awesome Project"
        p = Project(title)
        assert p.title == title


class TestTaskCreation:
    klass = Task

    def test_basic_creation(self):
        text, desc = 'lorem', 'ipsum dolor'
        s = self.klass(text=text, description=desc)
        assert s.text == text
        assert s.description == desc

    def test_fresh_instance_has_empty_parent(self):
        t = self.klass('saynomore')
        assert t.parent is None


class TestStoryCreation(TestTaskCreation):
    klass = Story

    def test_fresh_story_has_empty_subtasks_list(self):
        s = self.klass('hello')
        assert s.subtasks == []


class TestAddingSubtask:
    def test_adding_task(self, story, task):
        story.add_subtask(task)
        assert task in story.subtasks

    def test_added_task_has_parent_set(self, story, task):
        story.add_subtask(task)
        assert story is task.parent

    def test_adding_subtask_is_idempotent(self, story, task):
        story.add_subtask(task)
        story.add_subtask(task)
        assert story.subtasks.count(task) == 1

    def test_adding_to_one_story_removes_subtask_from_another(self, task):
        story_a, story_b = Story('lorem'), Story('ipsum')
        story_a.add_subtask(task)
        story_b.add_subtask(task)
        assert task not in story_a.subtasks


class TestRemovingTask:
    def test_removing_removes_parent(self, task_with_story):
        s = task_with_story.parent
        s.remove_subtask(task_with_story)
        assert task_with_story.parent is None


# factories
def pytest_funcarg__story(request=None):
    return Story('As a user ...')

def pytest_funcarg__task(request=None):
    return Task('Prepare initial repository')

def pytest_funcarg__task_with_story(request=None):
    s = pytest_funcarg__story()
    t = pytest_funcarg__task()
    s.add_subtask(t)
    return t
