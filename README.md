# Random TfL Journey Planner

 Generate randomised journeys to take on the TfL network! Random TfL Journey Planner is a Flask-based web app that invents a random journey, then pulls data from the Tfl API, showing the steps of how to take the journey.
 
 ## Tech Stack
 
 The app runs on a Flask backend with an [Adapt UI](https://docs.liveg.tech/?product=adaptui&page=index.md) frontend. Adapt UI is LiveG's "user interface library and design language for building consistent and appealing products". I used it for this project because, well, I'm on the LiveG staff team and it'd be wrong not to.
 When you load the page, Flask serves you a static HTML page with Adapt UI's CSS taking care of the UI layout. As soon as you click the Generate Journey button, JavaScript running in your browser makes a request back to the Flask server on `/journey`. The Flask server chooses two random stations, calls the TfL API to calculate the journey, then returns the journey information to the JavaScript running in the browser. The JavaScript then inserts the data into the placeholder card, and if the app could not find the journey for whatever reason, it inserts an error message and logs the failed response to the console.
 
 ## Install
 
 ### Clone this repo
 
 ```
 git clone https://github.com/tramcrazy/Random-TfL-Journey/
 ```
 
 ### Grab a TfL API key
 
 - Go [here](https://api-portal.tfl.gov.uk/).
 - Click sign in, then sign up.
 - Once you're signed up and logged in, go to this [product page](https://api-portal.tfl.gov.uk/product#product=2357355709892).
 - Come up with a name for the subscription (maybe RandomJourney) and hit Subscribe.
 - Go to your [profile](https://api-portal.tfl.gov.uk/profile).
 - In Subscriptions, click Show next to the Primary Key - that string of letters and numbers is your key.
 
 ### Change into the right directory
 
 ```
 cd Random-TfL-Journey
 ```
 
 ### Set the API key as an environment variable
 
 #### Linux/macOS (Bash)
 
 ```
 export TFL_API_KEY=yourapikeygoeshere
 ```
 
 #### Windows (PowerShell)
 
 ```
 $Env:TFL_API_KEY = "yourapikeygoeshere"
 ```
 
 ### Install dependencies
 
 ```
 pip install -r requirements.txt
 ```
 
 ### Run!
 
 ```
 flask run
 ```
 
 ## Test
 Visit [http://localhost:5000](http://localhost:5000)
 Try clicking the generate journey button.
 Wait a few seconds and a journey should appear!
 If you get an error, keep trying as the system isn't perfect!
 
 ## Credits
 I used a snippet of [Josh Blewitt's code](https://gitlab.com/JoshBl_/python/-/blob/2d873b2f251be8d34d69f411fb7a7931a27ca61d/TfL%20App/tfl-app.py) for help with parsing the TfL API responses.
