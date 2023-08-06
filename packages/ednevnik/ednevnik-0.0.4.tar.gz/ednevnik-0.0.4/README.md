# E-Dnevnik API
Kinda slow (avarage 3 seconds) ednevnik api for getting user information.

### Requirements 
* selenium
* webdriver (needs to be installed via following link https://chromedriver.chromium.org/downloads)

### Description
* `auth` function returns if given username and password are real/correct.
* `grade` function returns which class a given user is.
* `nameSurname` function returns a name and surname of given user.
* `userInfo` function returns all info of a given user. (output is given in a list, first element is user class, second element is name and surname, third element is ordinal number of a user)
* `userNumber` function returns ordinal number if a user.
* `getClassYear` function returns current class year.
* `getSchool` function returns current class year.

### Example Code 1
```py
import ednevnik

username = "jeremy.clarkson@skole.hr"
password = "76ghBI7g"
path = "C:\Users\James\chromedriver.exe"        #path is your personal path where webdriver is located on your PC

dnevnik = ednevnik.ednevnik(username,password,path)

userClass = dnevnik.grade()
print(userClass)
```
### Example Code 2
```py
import ednevnik

username = "james.may@skole.hr"
password = "09OIjs65"
path = "C:\Users\James\Programs\chromedriver.exe"       #path is your personal path where webdriver is located on your PC

dnevnik = ednevnik.ednevnik(username,password,path)

authentication = dnevnik.auth()
if authentication == True:
    print('User is valid.')
else:
    print("User info is incorrect or doesn't exist.")
```
### Example Code 3
```py
import ednevnik

username = "richard.hammond@skole.hr"
password = "9865Y7jH"
path = "C:\Users\Richard\Modules\chromedriver.exe"       #path is your personal path where webdriver is located on your PC

dnevnik = ednevnik.ednevnik(username,password,path)

userInformation = dnevnik.userInfo()
print(userInformation)
```