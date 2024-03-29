from os import path

from flask import Flask
from flask_graphql import GraphQLView

from sqlalchemy.orm import Session

from DB.orm.db_session import db_session
from DB.schema import schema, Employee, Injury, JobClass, PrimaryDepartment, SecondaryDepartment, WorkStatus
from DB.helpers.build_up import build_up

app = Flask(__name__)
app.debug = True

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True,
        get_context=lambda: {'session':db_session}
    )
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    if not path.exists('./test.db'):
        build_up()
    app.run()