import radius
from loguru import logger
import argparse


def main(user, pwd, secret, host, port):

  r = radius.Radius(secret, host=host, port=port)

  try:
      logger.info('successfully authenticated' if r.authenticate(username, password) else 'failure')
      sys.exit(0)
  except radius.ChallengeResponse as e:
      logger.error(f'An error occurred: {e}')

  # The ChallengeResponse exception has `messages` and `state` attributes
  # `messages` can be displayed to the user to prompt them for their
  # challenge response. `state` must be echoed back as a RADIUS attribute.

  # Send state as an attribute _IF_ provided.
  attrs = {'State': e.state} if e.state else {}

  # Finally authenticate again using the challenge response from the user
  # in place of the password.
  logger.info('success' if r.authenticate(username, response, attributes=attrs)
                  else 'failure')

  
  # Another way

  r = radius.authenticate(secret, username, password, host=host, port=port)
  logger.tracer(r)
  
  
if __name__ == "__main__":
  
  parser = argparse.ArgumentParser(description='RADIUS Challenge/Response Authentication')
  parser.add_argument('user', type=str, help='user id (e.g. MU59145)')
  parser.add_argument('pwd', type=str, help='user password')
  parser.add_argument('secret', type=str, help='RADIUS Secret')
  parser.add_argument('host', type=str, help='RADIUS server hostname/IP')
  parser.add_argument('port', type=int, help='RADIUS server port', default=1812)

  args = parser.parse_args()
  user = args.user
  pwd = args.pwd
  secret = args.secret
  host = args.host
  
  main(user, pwd, secret, host)
