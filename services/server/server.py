import flask

from services.web.route.customer import customer
from services.web.route.host import host
from services.web.route.index import index

server = flask.Flask(__name__)


server.register_blueprint(customer)
server.register_blueprint(host)
server.register_blueprint(index)


def main():
    server.run()


if __name__ == '__main__':
    main()

