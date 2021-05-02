import argparse
import sys
import traceback
from getpass import getpass

from loguru import logger

from radius import Attributes, ChallengeResponse, authenticate, NoResponse, SocketError


def main(username, password, secret, host, port=1812):
    def _status(outcome):
        if outcome:
            print("Authentication Succeeded")
            sys.exit(0)
        else:
            sys.exit("Authentication Failed")

    err = None

    try:
        _status(authenticate(secret, username, password, host=host, port=port))
    except ChallengeResponse as e:
        err = e
    except NoResponse:
        sys.exit("No Response")
    except SocketError:
        sys.exit("Socket Error")
    except Exception:
        traceback.print_exc()
        sys.exit("Authentication Error")

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
        traceback.print_exc()
        sys.exit("Authentication Error")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="RADIUS Challenge/Response Authentication"
    )
    parser.add_argument("username", type=str, help="username id (e.g. MU59145)")
    parser.add_argument("host", type=str, help="RADIUS server hostname/IP")

    args = parser.parse_args()
    username = args.username
    host = args.host

    password = getpass("Enter your Password: ")
    secret = getpass("Enter RADIUS Secret: ")

    main(username, password, secret, host)
