# user_authentication
Registration and Login system with Python, file handling

STAGE : 1 
Registration

When the user chooses to Register
email/username should have "@" and followed by "."
password (5 < password length > 16)
              Must have minimum one special character,
              one digit,
              one uppercase, 
              one lowercase character 

Stage : 2

Once the username and password are validated, store those values in a file

Stage : 3
Login

When the user chooses to Login, check whether his/her credentials exist in the file or not based on the user input 
If doesn’t exist ask them to go for Registration or 
If they have chosen forget password you should be able to retrieve their original password based on their username provided in the user input
If nothing matches in your file you should ask them to Register
