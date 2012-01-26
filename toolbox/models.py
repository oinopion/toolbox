# encoding: utf-8

class ModelError(Exception):
    """ Standard model error """


class Model(object):
    """ Base class for all business models """


class User(Model):
    def __init__(self, email):
        self.email = email
        self.projects = []
        self.created_projects = []

    def create_project(self, name):
        project = Project(creator=self, name=name)
        self.projects.append(project)
        self.created_projects.append(project)
        return project


class Project(Model):
    def __init__(self, creator, name):
        self.creator = creator
        self.name = name
        self.users = [creator]

    def add_user(self, user):
        self.users.append(user)
        user.projects.append(self)

