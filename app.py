from todoapp import create_app
from todoapp.extentions import db, jwt


app=create_app()
# Initialize database and JWT with the app
db.init_app(app)
jwt.init_app(app)

from todoapp.routes.auth import auth
app.register_blueprint(auth)
from todoapp.routes.api import api
app.register_blueprint(api)



if __name__ == '__main__':
    # Create database tables within the application context
    with app.app_context():
        db.create_all()
    
    # Run the app
    app.run(host='0.0.0.0', port=8080, debug=True)
