# MVPlayer

MVPlayer is a website developed on pythons django framework, provided functionality on a music website

## To Deploy Project

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

First create a virtual environment and activate it, then install all the required dependencies of the project.

```bash
pip install -r /path/to/requirements.txt
```
If database isn't there which will not be there in future, migrates all the changes if needed.
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```


## Screenshots
![alt text](https://github.com/vik-negi/sangeet/blob/main/staticfiles_build/screenshots/home1.png)\
![alt text](https://github.com/vik-negi/sangeet/blob/main/staticfiles_build/screenshots/home2.png)\
![alt text](https://github.com/vik-negi/sangeet/blob/main/staticfiles_build/screenshots/all_songs.png)&nbsp;&nbsp;
![alt text](https://github.com/vik-negi/sangeet/blob/main/staticfiles_build/screenshots/register.png)&nbsp;&nbsp;
![alt text](https://github.com/vik-negi/sangeet/blob/main/staticfiles_build/screenshots/login.png)&nbsp;&nbsp;


Please make sure to update tests as appropriate.

## License

[MIT](https://github.com/vikramnegiofficial/MVPlayer/blob/main/LICENSE.md)
