# services/users/manage.py

import unittest

from flask.cli import FlaskGroup

from project import create_app, db
from project.api.models import User


app = create_app()
cli = FlaskGroup(create_app=create_app)


# for some reason, recreate_db cannot be called from cli but recreatedb works
@cli.command()
def recreatedb():
    # call the original recreate_db() function
    recreate_db()


def recreate_db():
    # Recreate the db
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command()
def test():
    """Runs the tests without code coverage"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0

    return 1


if __name__ == '__main__':
    cli()
