from flask import Flask, render_template
from flask.ext.debugtoolbar import DebugToolbarExtension
import pymongo
import os
import sys

sys.path.append(os.path.abspath('.'))

app = Flask(__name__)
app.debug = True
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'u=0tir)ob&3%uw3h4&&$%!!kffw$h*!_ia46f)qz%2rxnkhak&'
app.config['DEBUG_TB_PANELS'] = (
    'flask_debugtoolbar.panels.versions.VersionDebugPanel',
    'flask_debugtoolbar.panels.timer.TimerDebugPanel',
    'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
    'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
    'flask_debugtoolbar.panels.template.TemplateDebugPanel',
    # 'flask_debugtoolbar.panels.sqlalchemy.SQLAlchemyDebugPanel',
    'flask_debugtoolbar_mongo.panel.MongoDebugPanel',
    'flask_debugtoolbar.panels.logger.LoggingPanel',
    'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel',
)
app.config['DEBUG_TB_MONGO'] = {
     'HIDE_FLASK_FROM_STACKTRACES': False
}
DebugToolbarExtension(app)

conn = pymongo.Connection()
db = conn.debug_test


@app.route('/')
def index():
    #list(db.test.find({'name': 'test'}))
    db.test.find({'name': 'test'}).count()
    db.test.find({'name': 'test'}).count()
    list(db.test.find({'name': 'test', 'age': {'$lt': 134234}}).skip(1))
    db.test.find({'name': 'test'}).count()
    db.test.find({'name': 'test'}).skip(1).count(with_limit_and_skip=True)
    list(db.test.find({'name': 'test'}).sort('name'))
    sort_fields = [('name', pymongo.DESCENDING), ('date', pymongo.ASCENDING)]
    list(db.test.find({'name': 'test'}).sort(sort_fields))
    list(db.test.find({
        '$or': [
            {
                'age': {'$lt': 50, '$gt': 18},
                'paying': True,
            },
            {
                'name': 'King of the world',
                'paying': False,
            }
        ]
    }))
    db.test.insert({'name': 'test'})
    db.test.insert({'name': 'test2'}, safe=True)
    db.test.update({'name': 'test2'}, {'age': 1}, upsert=True)
    db.test.remove({'name': 'test1'})
    return render_template('index.html')

if __name__ == '__main__':
    app.run('127.0.0.1', 8081)
