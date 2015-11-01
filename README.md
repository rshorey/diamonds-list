# diamonds-list
Diamond's List is a way to connect people with service needs to returning citizens that can assist them. 

The goals are 1) to provide affordable assistance to communities and organizations in need, and 2) to help returning citizens get to work and become self-sufficient.

Available services include repairs (e.g., home, auto), maintenance (e.g., cleaning, landscaping) or freelance projects (e.g., digital services, advocacy speakers).


* Using Python3/postgres
* create virtual environment using python 3
* pip install -r requirements.txt
* createuser diamondslist -s
* createdb diamondslist -U diamondslist
* Edit the virtualenv's postactivate file (instructions below from commandline with sublime, any text editor works):
* subl $VIRTUAL_ENV/bin/postactivate
* Paste in the following:

  ```export HEROKU_DB_NAME='diamondslist'
  export HEROKU_DB_USER='diamondslist'
  export HEROKU_DB_PASSWORD=''
  export HEROKU_DB_HOST='localhost'
  export DJANGO_DEBUG=True
  export SECRET_KEY='any_string_here'```
  
* Deactivate your virtual environment, and then reactivate
* You should be able to run, but let me know if I forgot something!
