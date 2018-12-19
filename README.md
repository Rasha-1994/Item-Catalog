

# Item Catalog
## Project Description
A simple web application is a project for the Udacity's Full Stack Web Developer Nanodegree.
This application provides a list of items within a variety of categories and integrate third party user registration and authentication. Authenticated users have the ability to post, edit, and delete their own items.

## Prerequisites
1. Python 3.5.2
2. Vagrant
3. VirtualBox


## How to Run
1. Install VirtualBox and Vagrant
2. Clone this repo
3. Unzip the folder
4. Launch the Vagrant VM from inside the *vagrant* folder with:

`vagrant up`

5. Then access the shell with:

`vagrant ssh`

6. Then move inside the catalog folder:

`cd /vagrant/catalog`

7. Then run the application:

`python application.py`

8. Open the browser and go to this URL:

`http://localhost:8000/`
## Helpful Resources
- [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [Vagrant](https://www.vagrantup.com/downloads.html)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- [Full Stack Foundations](https://classroom.udacity.com/courses/ud088)
- [Authentication and Authorization](https://classroom.udacity.com/courses/ud330)
