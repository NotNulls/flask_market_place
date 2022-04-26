from market import app,db
from market.models import Item, User

if __name__ == '__main__':
    app.run(debug=True)

@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'User': User, 'Item': Item}