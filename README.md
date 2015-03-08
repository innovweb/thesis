thesis
======

Princeton Innovation's Senior Thesis Project Repository

Requires: Python2.7 and Django1.7

## To test on local machine:
From command line run: `python manage.py runserver`
You should see output that looks like:
```
Performing systems checks...

System check identified no issues (0 silenced).
March 08, 2015 - 17:36:42
Django version 1.7.4 using settings 'thesis.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK
```

This will run the server on Port 8000 (port can be changed under thesis/settings) and can be accessed at http://localhost:8000/articles/

## To scrape (rebuild the database):
The original senior theses can be found at: http://dataspace.princeton.edu/jspui/

scrapeToDatabase.py will run a script to scrape the theses into the project's database.  You can edit the `num_to_scrape` and `year` variables to specify the number of articles to scrape and from which year. Note that the script takes a while to run (approximately a minute on 100 theses). Currently, the script runs for all the 2014 theses (of which there are 1189).