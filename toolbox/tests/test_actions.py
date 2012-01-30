# encoding: utf-8
from mock import Mock
from toolbox.actions import CreateUser, CreateProject, AddUserToProject
from toolbox.tests.creators import create_user, create_project

class ActionTest(object):
    action_class = None

    def setup(self):
        self.stores = Mock()

    def action(self, *args, **kwargs):
        action = self.action_class(*args, **kwargs)
        action.stores = self.stores
        return action


class TestCreateUserAction(ActionTest):
    action_class = CreateUser

    def test_creates_user(self):
        action = self.action('alice@example.com')
        action.perform()
        user = self.stores.users.add.call_args[0][0]
        assert user.email == 'alice@example.com'


class TestCreateProjectAction(ActionTest):
    action_class = CreateProject

    def test_creates_project_for_given_user(self):
        user = create_user()
        name = "Project One"
        action = self.action(user=user, project_name=name)
        action.perform()
        project = self.stores.projects.add.call_args[0][0]
        assert project.name == name


class TestAddUserToProjectAction(ActionTest):
    action_class = AddUserToProject

    def test_adds_user_to_project(self):
        user = create_user()
        project = create_project()
        action = self.action(user=user, project=project)
        action.perform()
        assert user in project.users
