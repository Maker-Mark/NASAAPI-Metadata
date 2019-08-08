[![Build Status](https://travis-ci.org/Maker-Mark/NASAAPI-Metadata.svg?branch=master)](https://travis-ci.org/Maker-Mark/NASAAPI-Metadata)
# Setup
- Option one: Deployed on Heroku with continuios integration here: https://nasaapi-metadata.herokuapp.com
- Option two: Local machine
If you're using a virtual environment, activate it and install the dependencies via a `pip install -r requirements.txt`.
Note: You may need to try `pip3 install -r requirements.txt`

## Running the Program

Simply navigate to the app folder with a `cd app` and run the app via `python app.py` or `python3 app.py`
The application should be running at `http://127.0.0.0:5000/` or `localhost:5000`


## Setting up Continious Integration with Travis CI
- The main challenge of acheiving this was configuring a `.travis.yml` in  the current github repository
  - The `.travis.yml` allows us to specify install instructions, as well as script instructions.
      - When building, you're often going to need to chage folder's first, or do some sort of check(conditional) before executing.
 ## See an example of a travis.yml
 ``` 
dist: xenial   # Specify the distrebution
language: python
python:
  - "3.7"
  - "3.7-dev"  # 3.7 development branch
  - "3.8-dev"  # 3.8 development branch
  - "nightly"  # nightly build
# command to install dependencies
install:
  - pip install -r requirements.txt
# The before_script will run the follwing commands before continuing to the script section  
before_script: cd app
# command to run unit tests  and so on
script:
  - python test.py 
  ```
  - As you can see, getting started with Trivis is not too bad, and gives you a easy, recorded way of seeing what code builds.
### Deploying
  - Deploying a flask application is not too bad, there are a few platforms, heroku, netlify, python anywhere and google app engine (to mention a few)
  - For example, you can acheive a successful deploy with just an addition of the deploy clause in the `.travis.yml`
 file.
 ```
 deploy:
  provider: heroku
  api_key:
    secure: "YOUR HEROKU KEY HERE"
  app: NAME OF HEROKU APP ( ie nasa-api-3140heroku )
  on:
    repo: Maker-Mark/NASAAPI-Metadata
 ```
 ### Continuoius Integration and Deployment
  - As long as you configure your `.travis.yaml` correctly, you should be up and running!
  - Just enable automatic deploys and set the continious integration check to true.
  [Imgur](https://imgur.com/XLdxumu)
 
# Congraduations! 
  - Your Flask App is now building from the .travis.yml and auto-deploying.
  - A trvis build will happen anytime the trigger goes off (ie a push to the selected branch)
    - Once a travis test passes, Heroku will automatically deploy, thanks to that .travis.yml deploy clause!
 ## Final Thoughts   
This excersise  was particularly challenging as the different tools require significant research to get basic examples going. It took me 4 different deploys and platforms to get somewhere, and I'm glad I did. I feel like I have gotten 100 times better at VIM and see the necessity for learning server-management command line tools, as well as the security vulnerabilities that are at stake .
