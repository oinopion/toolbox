# encoding: utf-8

class ModelError(Exception):
    """Standard model error"""


class Project(object):
    def __init__(self, title):
        self.title = title


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
        if subtask.parent is self:
            return
        if subtask.parent:
            subtask.parent.remove_subtask(subtask)
        self.subtasks.append(subtask)
        subtask.parent = self

    def remove_subtask(self, subtask):
        self.subtasks.remove(subtask)
        subtask.parent = None
