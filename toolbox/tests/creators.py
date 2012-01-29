from toolbox.models import User, Project

def create_user(email='alice@example.com'):
    return User(email=email)


def create_project(name='Project Manhattan', creator=create_user):
    if callable(creator):
        creator = creator()
    return Project(name=name, creator=creator)
