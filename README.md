#Web Scraping using Django
In this project you can see web scraping with django. We can easily call an api and scrap the articles from the website called theverge.com. After scraping data will be store in Sqlite database. And on daily this api runs and scrap the article on daily basis at 10:00, and keep storing articles in the database.

##API Reference
####To post the article, call the bellow api.
  ```
	http://54.199.170.96:8000/scraping/articles/
	```

####To see the data we call,
```
http://54.199.170.96:8000/admin/scraping/article/
```
##Appendix
This project is running on a cloud service AWS ec2. To login into admin to see Articles use:-

username = user_1
password = userpassword


##Setup
To get this repository, run the following command inside your git enabled terminal.

```
git clone https://github.com/Parassirohi/django_scraping
```
To install all of the Python modules and packages used in this project, run the following command inside your terminal.

```pip install -r requirements.txt```
