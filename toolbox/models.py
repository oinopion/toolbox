# encoding: utf-8

class ModelError(Exception):
    """Standard model error"""

class SubtaskError(ModelError):
    """Raised if subtask cannot be added"""


class Task(object):
    def __init__(self, text, description=""):
        self.text = text
        self.description = description
        self.parent = None


class Story(Task):
    def __init__(self, text, description=""):
        super(Story, self).__init__(text, description)
        self.subtasks = []

    def add_subtask(self, subtask):
        if self.parent:
            raise SubtaskError()
        if subtask.parent:
            subtask.parent.subtasks.remove(subtask)
        if not subtask in self.subtasks:
            self.subtasks.append(subtask)
        subtask.parent = self

    def remove_subtask(self, subtask):
        self.subtasks.remove(subtask)
        subtask.parent = None
