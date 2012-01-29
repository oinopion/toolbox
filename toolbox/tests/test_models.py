from datetime import timedelta
from mock import sentinel
from toolbox.models import User, Project
from toolbox.tests.creators import create_user, create_project


class TestUserModel:
    def test_user_has_email(self):
        email = 'bob@example.com'
        user = User(email=email)
        assert user.email == email

    def setup(self):
        self.user = create_user()

    def test_new_user_has_no_created_projects(self):
        assert self.user.created_projects == []

    def test_create_project_with_name_has_user(self):
        name = 'Awesome project'
        project = self.user.create_project(name)
        assert project.creator == self.user

    def test_create_project_adds_it_to_created_projects(self):
        project = self.user.create_project(name='Awesome project')
        assert project in self.user.created_projects

    def test_create_project_adds_it_to_projects_list(self):
        project = self.user.create_project(name='Awesome project')
        assert project in self.user.projects

    def test_new_user_has_empty_projects_list(self):
        assert self.user.projects == []


class TestProjectModel:
    def test_project_has_creator_and_name(self):
        name = 'Test project'
        project = Project(creator=sentinel.User, name=name)
        assert project.name == name
        assert project.creator == sentinel.User

    def setup(self):
        self.project = create_project()

    def test_new_projects_users_contains_creator_only(self):
        assert self.project.users == [self.project.creator]

    def test_add_user_to_project_adds_him_to_project_users_list(self):
        other_user = create_user('bob@example.com')
        self.project.add_user(other_user)
        assert other_user in self.project.users

    def test_add_user_to_project_adds_it_to_users_projects_list(self):
        other_user = create_user('bob@example.com')
        self.project.add_user(other_user)
        assert self.project in other_user.projects

    def test_default_sprint_length_is_one_week(self):
        assert self.project.default_sprint_length == timedelta(days=7)

    def test_next_sprint_start_is_none(self):
        assert self.project.next_sprint_start_date is None
