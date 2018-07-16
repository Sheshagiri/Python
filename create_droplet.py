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

    #give name that you want to name your droplet.
    #Most important this is the image, you need to provide the id of the image, NAME OF THE IMAGE DOESN'T WORK.
    data = '{"name":"example2.com","region":"blr1","size":"s-1vcpu-1gb","image":"36278887","ssh_keys":null,"backups":false,"ipv6":true,"user_data":null,"private_networking":null,"volumes": null,"tags":["web"]}'

    create_droplet_url = _base_url+'droplets'
    
    create_droplet = requests.post(create_droplet_url,data=data,headers=_my_auth)

    #prints the status of the rest call
    #print create_droplet.status_code

    if create_droplet.status_code == 202:
    	print "Droplet created successfully."
    	parsed_json = json.loads(create_droplet.text)
    	print "Droplet Id is : "+str(parsed_json['droplet']['id'])
    else:
    	print "There was a error while creating the droplet."
    	print "--------------Response-----------------------"
    	print json.dumps(create_droplet.json(), indent=4, sort_keys=True)