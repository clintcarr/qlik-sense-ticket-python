"""
Example Qlik Sense Ticket code
"""

import argparse
import json
import random
import string
import webbrowser
import requests

parser = argparse.ArgumentParser()
parser.add_argument('--server', help='Qlik Sense Server to connect to')
parser.add_argument('--certs', help='Location of certificates')
parser.add_argument('--virtualproxy', help='Qlik Sense Virtual Proxy')
parser.add_argument('--user', help='user')
parser.add_argument('--userdirectory', help='directory to append')

args = parser.parse_args()

requests.packages.urllib3.disable_warnings()

def set_xrf():
    """
    Create XRF key used to prevent cross site request forgery
    """
    characters = string.ascii_letters + string.digits
    return ''.join(random.sample(characters, 16))

xrf = set_xrf()
certificate=(args.certs+'/client.pem', args.certs+'/client_key.pem')
root = root=args.certs+'/root.pem'
headers = {'content-type': 'application/json',
           'X-Qlik-Xrfkey': xrf,
          }

def get_ticket():
    """
    Post arguments to the Qlik Sense Virtual Proxy
    :return: Ticket
    """
    payload = {'UserDirectory': args.userdirectory, 'UserId': args.user}
    json_payload = json.dumps(payload)
    url = 'https://{0}:4243/qps/ticket?Xrfkey={1}'.format(args.server, xrf)
    if args.virtualproxy is not None:
        url = 'https://{0}:4243/qps/{1}/ticket?Xrfkey={2}'.format(args.server, args.virtualproxy, xrf)
    response = requests.post(url, data=json_payload, headers=headers, verify=root, cert=certificate)
    return response.json().get('Ticket')

def create_url():
    """
    Construct the URL with the Qlik Sense Ticket
    """
    url = 'https://{0}/hub/?qlikTicket={1}'.format(args.server, get_ticket())
    if args.virtualproxy is not None:
        url = 'https://{0}/{1}/hub/?qlikTicket={2}'.format(args.server, args.virtualproxy, get_ticket())
    return url

if __name__ == '__main__':
    webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(create_url())
