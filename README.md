# HashTag Battles App

## Setup and Run


1. Create an Ubuntu 14.04 instance on Digital Ocean / AWS / localhost & connect via ssh

2. `sudo apt-get update && sudo apt-get install git docker.io`

3. `git clone https://github.com/https://github.com/torrange/bnd.git

4. `cd ./bnd/bynd/ && sudo docker build .`

5. `sudo docker run --net=host -d -t <image_build_id>`

6. Open [http://{{digital_ocean_ip:8000/admin}}/](http://127.0.0.1:8000/admin) or [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) in a browser.

7. Login as:
    1. `admin`
    2. password sent privately

8. To access the API battles endpoint:
    1. JSON: make a get request to: [http://127.0.0.1:8000/api/battle/4/?format=json](http://127.0.0.1:8000/api/battle/4/?format=json) to retrieve information for BattleID #4
    1. XML : make a get request to: [http://127.0.0.1:8000/api/battle/4/?format=xml](http://127.0.0.1:8000/api/battle/4/?format=XML) to retrieve information for BattleID #4

9. To view the Public Battles
    1. [http://127.0.0.1:8000/battles/](http://127.0.0.1:8000/battles/)
    
10. Additional improvements to implement`
    1. Extend the TastyPie API to accept POST requests for Battle creation
    2. Add some visual sugar to the public /battles/ view
    3. Register the API in Django Admin for API Key storage

These steps can be followed verbatim on [http://localhost/] (http://localhost/) running an instance of the docker.io daemon

