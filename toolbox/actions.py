from toolbox.models import User

class Action(object):
    """ Base action class """
    stores = None

    def perform(self):
        return self.run()

    def run(self):
        """ Implement in subclasses """
        raise NotImplementedError


class CreateUser(Action):
    def __init__(self, email):
        self.user = User(email=email)

    def run(self):
        self.stores.users.add(self.user)


class CreateProject(Action):
    def __init__(self, user, project_name):
        self.user = user
        self.project_name = project_name

    def run(self):
        project = self.user.create_project(self.project_name)
        self.stores.projects.add(project)


class AddUserToProject(Action):
    def __init__(self, project, user):
        self.project = project
        self.user = user

    def run(self):
        self.project.add_user(self.user)
