
# make migrations
python manage.py makemigrations bootstrap_simple_note_app

# migrate
python manage.py migrate bootstrap_simple_note_app

# run server
python manage.py runserver


http://127.0.0.1:8000/bootstrap-notes/

http --print HBhb GET http://127.0.0.1:8000/bootstrap-notes/api/v1/notes/ timestamp==1526927580.0
