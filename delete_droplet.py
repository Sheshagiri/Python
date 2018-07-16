import requests
import json
import sys

#put your own token, open https://cloud.digitalocean.com/settings/api/tokens in your favourite browser to generate token.
_token = '<Redacted>'
_base_url = 'https://api.digitalocean.com/v2/'

_my_auth = {
  		'Authorization': 'Bearer '+_token,
  		'Content-Type': 'application/json'
	}


if __name__ == '__main__':

    if not _token:
        sys.stderr.write("Token is required to continue. Get it at https://cloud.digitalocean.com/settings/api/tokens. You need to be an Administrator\n")
        sys.exit()

    if not _base_url:
        sys.stderr.write("url is required to connect to digitalocean.\n")
        sys.exit()

    
    user_info_url = _base_url+'account'
    
    user_info = requests.get(user_info_url,headers=_my_auth)

    #print user_info.status_code
    #check if the token is valid
    if user_info.status_code == 200:
    	sys.stderr.write("Authentication successfull.\n")
    else:
    	sys.stderr.write("There was an error while authenticating.\n")
    	print json.dumps(user_info.json(), indent=4, sort_keys=True)
    	sys.exit()

    droplet_id = ''
    if sys.argv == 0:
    	sys.stderr.write("droplet id is required to delete a droplet.\n")
        sys.exit()
    else:
    	droplet_id=sys.argv[1]

    delete_droplet_url = _base_url+'droplets/'+droplet_id
    
    #print delete_droplet_url
    delete_droplet = requests.delete(delete_droplet_url,headers=_my_auth)

    if delete_droplet.status_code == 204:
    	print "Droplet "+droplet_id+" is deleted."
    else:
    	print "There was a error while deleting the droplet."
    	print "--------------Response-----------------------"
    	print json.dumps(delete_droplet.json(), indent=4, sort_keys=True)
        