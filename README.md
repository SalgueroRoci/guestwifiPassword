Using Ubuntu 18 
latest Chrome version (80)
latest selenium version 

# install python and pip
sudo apt-get update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.7
sudo apt install python3-pip

# install dependancies
sudo pip3 install -r requirements.txt

# Install google chrome
sudo apt-get update
sudo apt-get install libgconf2-4 libnss3-1d libxss1
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt-get install -f
google-chrome --version

# Get webdriver for selenium from https://chromedriver.chromium.org/getting-started
# unzip in same folder as project

# make a config.py file with username and password
VPNusername="<username>"
VPNpassword="<password>"
SSOusername="<username>"
SSOpassword="<password>"
Webhook="<Slack URL>"

# Run python code 
nohup guestPW.py

