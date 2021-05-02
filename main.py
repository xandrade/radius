import argparse
import traceback
from getpass import getpass

from loguru import logger

import radius


def main(username, password, secret, host, port=1812):

    try:
        r = radius.authenticate(
            secret=secret, username=username, password=password, host=host, port=port
        )
        logger.tracer(type(r))
        logger.tracer(r)
        logger.tracer(r.__dict__)
        logger.tracer(r.__class__)

    except radius.ChallengeResponse as e:
        logger.info(f"Successfully authenticated. State={e.state}")
    except Exception as e:
        logger.error(f"An error occurried: {e}")
    except:
        logger.error(traceback.print_exc)


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
