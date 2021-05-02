import argparse

from loguru import logger

import radius


def main(username, password, secret, host, port):

    try:
        r = radius.authenticate(secret, username, password, host=host, port=port)
        logger.tracer(type(r))
        logger.tracer(r)
        logger.tracer(r.__dict__)
        logger.tracer(r.__class__)

    except Exception as e:
        logger.error(f"An error occurried: {e}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="RADIUS Challenge/Response Authentication"
    )
    parser.add_argument("username", type=str, help="user id (e.g. MU59145)")
    parser.add_argument("password", type=str, help="user password")
    parser.add_argument("secret", type=str, help="RADIUS Secret")
    parser.add_argument("host", type=str, help="RADIUS server hostname/IP")
    parser.add_argument("port", type=int, help="RADIUS server port", default=1812)

    args = parser.parse_args()
    username = args.username
    password = args.password
    secret = args.secret
    host = args.host
    port = args.port

    main(username, password, secret, host, port)
