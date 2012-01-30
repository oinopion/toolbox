# encoding: utf-8

class UserStore(object):
    def add(self, obj):
        raise NotImplementedError


class ProjectStore(object):
    def add(self, obj):
        raise NotImplementedError


class InMemoryUserStore(UserStore):
    def add(self, obj):
        return obj


class InMemoryProjectStore(ProjectStore):
    def add(self, obj):
        return obj
