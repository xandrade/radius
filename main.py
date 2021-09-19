from argparse import ArgumentParser
from sys import exit
from traceback import print_exc
from getpass import getpass

from loguru import logger

from radius import Attributes, ChallengeResponse, authenticate, NoResponse, SocketError


def main(username, password, secret, host, port):
    def _status(outcome):
        if outcome:
            print("Authentication Succeeded")
            exit(0)
        else:
            exit("Authentication Failed")

    err = None

    try:
        _status(authenticate(secret, username, password, host=host, port=port))
    except ChallengeResponse as e:
        err = e
    except Exception:
        print_exc()
        exit("Authentication Error")

    print("RADIUS server replied with a challenge.")

    for m in getattr(err, "messages", []):
        print(" - %s" % m)

    response = None
    while not response:
        response = getpass("Enter your challenge response: ")

    state = getattr(err, "state", None)
    a = Attributes({"State": state} if state else {})

    try:
        _status(
            authenticate(secret, username, response, host=host, port=port, attributes=a)
        )
    except Exception:
        print_exc()
        exit("Authentication Error")


if __name__ == "__main__":

    parser = ArgumentParser(description="RADIUS Challenge/Response Authentication")
    parser.add_argument("--username", type=str, help="username id (e.g. antonio)")
    parser.add_argument("--host", default="192.168.1.1", type=str, required=False, help="RADIUS server hostname/IP")
    parser.add_argument(
        "--port", default=1812, type=int, required=False, help="RADIUS server port"
    )

    args = parser.parse_args()
    username = args.username
    host = args.host
    port = args.port

    password = getpass("Enter your Password: ")
    secret = getpass("Enter RADIUS Secret: ")

    main(username, password, secret, host, port)
