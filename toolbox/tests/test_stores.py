# encoding: utf-8
from toolbox.stores import InMemoryUserStore, InMemoryProjectStore
from toolbox.tests.creators import create_user, create_project

class UserStoreTest:
    store = None

    def test_add_returns_user(self):
        user = create_user()
        assert self.store.add(user) is user


class TestInMemoryUserStore(UserStoreTest):
    def setup(self):
        self.store = InMemoryUserStore()



class ProjectStoreTest:
    store = None

    def test_add_returns_project(self):
        project = create_project()
        self.store.add(project)


class TestInMemoryProjectStore(ProjectStoreTest):
    def setup(self):
        self.store = InMemoryProjectStore()
