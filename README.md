# Random Photo Tweeter

## Dependencies
**Tweepy:** [tweepy](https://github.com/tweepy/tweepy)

## Introduction
Thee Random Photo Tweeter will automatically select a random photo from a file  of your choice and tweet it to your account along with a random status depending on the day of the week. It remembers the last photo tweeted so never tweets the same photo twice in a row! 

**Beware:** Once set up the Random Photo Twitter will post to your Twitter page when run with **no confirmation** required

## Getting started
### Linking your phone to your account
To link the Random Photo Tweeter with your Twitter account you must have added your mobile phone to your Twitter account. 

		If you have done this already skip to the next stage
	
1. Go to your twitter setting page
2. Click the **Mobile** tab down the side
3. Select the region, enter your mobile number and click **continue**
4. Enter your validation code and click **Activate phone**

### Authenticating the program to use your twitter
<a name="auth"></a>
1. Start be heading to the [Twitter Application Management](https://apps.twitter.com/) page.
2. Click the **Create New App** button to link up this program with your account.
3. Enter the details for the program, then click the **Create your Twitter application** button.
				
		For the Website your Twitter page URL will be ok
4. On your application page click the **Keys and Access Tokens** tab and keep this page open as we will need the keys on this page to set up the program to post to your twitter account

5. Now run the program following the instructions and paste in your access keys from the last step when prompted

## The config file
Every file you use this program to tweet pictures from will have its own **config.json** allowing for both multiple Twitter accounts and statuses that fit the pictures in that file.

### The random statuses
The **config.json** file contains the possible statuses for selection. They are kept in the format below:

		"Monday": [
         "I love Mondays",
         "I cant believe its already Monday",
         "It's Monday"
      	]

These are the three default statuses the program will choose from, each on its own line, surrounded by quote marks **"** and with a comma **,**  separating each statuses line. 

You can freely edit, add or remove these as you see fit.

### The keys
The **config.json** file contains the four authentication keys you gave the program so it can authenticate and post the photo every time it is run. They should be left untouched, as if they are incorrect the authentication will fail and Twitter will not allow the photo to be posted to your account.

### The last picture
The last picture that was posted is saved under the name **picOld** so upon relaunching a different photo is posted from last time

### License		
The MIT License (MIT)
Copyright (c) 2016 James Doel

Project commissioned by Tawesoft 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
