# Guest WIFI Project

Guest wifi project which integrated corporate guest wifi password to office slack to help with productivity in the office. The python script retrieves the guest wifi password then posts it on office Slack as a bot message. 

**Installation on a cloud server:**
OS Ubuntu 18.0
latest Chrome version (version 80)
latest selenium version 

## Getting started
These instructions will help you set up the project on a server and integrate on slack to have it post the guest wifi for your workspace.
### Prerequisites
**Install python and pip**
```
sudo apt-get update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.7
sudo apt install python3-pip
```

**Install google chrome**
```
sudo apt-get update
sudo apt-get install libgconf2-4 libnss3-1d libxss1
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt-get install -f
google-chrome --version
```
Get webdriver for selenium from https://chromedriver.chromium.org/getting-started  
unzip in same folder as project

**Clone the repo**
```
git clone https://github.com/SalgueroRoci/guestwifiPassword.git
``` 
**Install python dependancies**
```
sudo pip3 install -r requirements.txt
```

**Make a config.py file with username and password**  
VPNusername="<username>"  
VPNpassword="<password>"  
SSOusername="<username>"  
SSOpassword="<password>"  
Webhook="<Slack URL>"  
### Deployment 
**Run python code**
```
nohup python3 guestPW.py &
```
