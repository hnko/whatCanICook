# whatCanICook

whatCanICook is an application for sending SMS's recipe using Twilio SMS API. When you send a message to the number XXXXX specifying what dish you want to cook and what are the ingredients you want to put the application will send you a few recipes with an url to the recipe's source.

## Requirements
For deploying the application you will need:
* Twilio account
* Twilio number
* Install the requirements.txt (```pip3 install -r requirements.txt```)


## Running
You will need to deploy the application to have the webhook running. You can use [Heroku](https://www.heroku.com/pricing).

If you want to run it in your local machine you can use [ngrok](https://ngrok.com/). For doing this you will need to:
1. Set config.json with your data (Twilio account SID, Twilio auth_token and Twilio phone number) You can get all the information from [your Twilio dashboard](https://www.twilio.com/console).

2. Run Flask
```bash
export FLASK_APP=main.py
flask run
```
3. Run ngrok
```bash
ngrok http 5000
```
4. Get the url given in the ngrok execution and update your message configuration for webhooks. At the end of the url add '/sms'. Example of how to fill the field: ```http://1e38fc5f3b56.ngrok.io/sms```
5. Send a message to the Twilio number with the following structure: 
*dish* <name of the dish you want to cook>
*ingredients* <ingredients you want to use in your dish separated by a comma>

```
dish pasta
ingredients tomato, cheese
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

https://first-app-nicow.herokuapp.com/
https://git.heroku.com/first-app-nicow.git