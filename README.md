# sukejuru
Anime Schedule

นายบุลากร จั่นบุญมี 6310682577  
นายกฤตกร ชัยรัตนารมย์ 6310682692   
นายณนฐ์ อังสุวพัฒนากุล 6310682700  
นายคมชาญ สาสนทาญาติ 6310682684  
นายจิรวัจฒ์ มุกด์สุวรรณ์ 6310611097 

#### About this Project:
- This project is made for subject CN331. This project we made a website that can link to all source of an anime and update anime premiere calendar. This website is made for poeple who love to watch anime alot and want a website to store all path of anime because sometime some company amy not include some of anime that you want to watch so it can link to it immediately.

This project is inspired by [hareshi.net](hareshi.net)

```bash
$ # Get the code
$ git clone https://github.com/6310682700/sukejuru.git
$ cd sukejuru
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules - SQLite Storage
$ pip3 install -r requirements.txt
$
$ # Change Directory to work directory
$ # cd reg_site
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Start the app - custom port
$ # python manage.py runserver 0.0.0.0:<your_port>
$
$ # Access the web app in browser: http://127.0.0.1:8000/
```

#### <ins>More Information:</ins>  
[Pivotal Tracker](https://www.pivotaltracker.com/n/projects/2609659)  
[Github Repository](https://github.com/6310682700/sukejuru)
[Heroku](https://sukejuru.herokuapp.com/)
