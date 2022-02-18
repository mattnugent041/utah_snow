# utah_snow_report

This program is used to send a text message containing snow report information using the Gmail SMTP server. This program has some limitations and necessary alterations before running as described in the Assumptions and Limitations section.

# Assumptions and Limitations
1. BEFORE RUNNING, you will need to populate the phone_numbers{} dictionary with the phone numbers and their respective carriers you want to send to. The program is built to loop through this dictionary, so you can enter as many as you would like in the format 'PhoneNumber{}':'carrier'. Associated carriers can be found in the messageConfig.py file.
3. This program is currently only built to send snow report information for five mountains in Utah; Snowbird, Solitude, Alta, Brighton, Poweder Mountain. You could add additional ones if you'd like by adjusting the resorts{} dictionary from the skiutah.com website.
4. This only works with the Gmail SMTP server, which assumes that you have a Gmail account. You will also need to ensure to 'allow less secure apps' in your Gmail settings for this to work.
5. In current state, once started, the program is scheduled to automatically run every day at 6:30 CST. This can be changed by adjusting the schedule.every().day.at() function. Alternatively, you could remove this line altogther and make a direct call to main() which will run the program ad-hoc.
6. The app also requires that you update line 27 of the code to your local version of ChromeDriver

# General Logic

To start, you'll be asked for a Gmail address and a password; this is the account which will be used to deliver the messaging.

This first sets the resorts to be searched in the resorts dictionary. Then, using Selenium in combination with BeautifulSoup4, the program opens the skiutah.com website, and searches for relevant information for the previously set resorts. Once found, this information is then added to the updated_info{} dictionary.

This dictionary is then turned into a string to be passed to the messageConfig.py file, to be sent via the Gmail SMTP server using the entered email and phone numbers.
