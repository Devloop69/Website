from flask import Flask # type: ignore
from views import views

app = Flask(__name__)
app.secret_key = "G@jj@R1234"
app.register_blueprint(views,url_prefix="/")

if __name__ == '__main__':
    app.run(debug=True,port=8000)
