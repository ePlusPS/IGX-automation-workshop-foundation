# IGX-automation-workshop-foundation

## Mac specific workstation Setup

1. Installing Homebrew  

   * Install XCode dev tools or check they are installed  
   > xcode-select --install

   * If you get the following, it's already installed  
   > xcode-select: error: command line tools are already installed, use "Software Update" to install updates

   * Install homebrew  
   > /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

   * Check the install  
   > brew -v
   > \# example output  
   > Homebrew 1.8.2

   * Install Cask
   > brew tap caskroom/cask

2. Check you have Python 2 and 3 installed from a bash shell  
   > python -V  \# show your default versions  

   > python2 -V \# shows your python2 version. If this fails try:  
   > python2.7 -V

   > python3 -V \# shows your python3 version. Otherwise:  
   > python3.7 -V

   If you don't have these installed:

   * Install python2  
   > brew install python@2

   * Install python3  
   > brew install python
