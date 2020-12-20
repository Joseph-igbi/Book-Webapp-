# Book-Library WebApp

### Resources:
* Trello Board: https://trello.com/b/Ydgv39X2/sfia-project-book-library-webapp-joseph-i
* Books data from kaggle: https://www.kaggle.com/meetnaren/goodreads-best-books
## Index
* [Scope & Objectives](#Project-Scope)
* [Architecture](#architecture)
* [Containerisation](#Containerisation)
* [Deployment](#deployment)
* [Front End Design](#front-end-design)



## Project Scope
The project objectives includes:
* Create a monolithic web app with CRUD functionalities
* Containerise the app using docker
* Automate deployment of the app using Jenkins 

The App created for this project is a Book library app with functionalities that include:
* Create a User account that stores:
  * *User First and Last Name*
  * *User Email*
  * *User Password*
* Login/Logout 
* View and update account details
* Create a personal shelf where books the user likes can be stored
* Add/Delete books from the personal shelf
* Alternatively log in as guest with the limitation of not being able to create a personal shelf
* Navigate through the book database and find details on books using the search bar

The project idea is illustrated in the below Use case diagram:
### Use Case Diagram
![usecase][usecase] 
## Architecture
### Entity Relationship Diagram
The final ERD as modelled below allows for the creation of shelves in the Shelf table and for the updating of shelves in the Book-shelf table with ShelfID creating a relationship between the two. The Many to One relationship between Users and Shelf means that each user can have multiple shelves whilst the One to Many relationship between Shelf and Book-shelf means that for each shelf created, multiple books can be added.
![ferd] 
## Containerisation
Using docker I was able to containerise the app. The first step towards this involved creating the Dockerfile which dictates the steps in building the container.
A docker-compose file was then created which uses the Dockerfile to build and run the container. As this project is Monolithic and requires only 1 container the docker-compose file isn't necessary however it still helps automate the build and removes the need to repeatedly type in the parameters needed for the project.
#### Image of docker-compose file
![docker]

I am currently working on deploying the app as a kubernetes cluster. I am able to deploy the app service as a cluster however the database is also containerized which would lead to multiple instances of the database being created in the kubernetes service which is not desirable. 

Methods of getting around this would either be to build my database without containerization using AWS RDS (i could use terraform/cloudformation to automate it) or ensure the database asynchronously replicates between the containers. 


## Deployment
### CI Pipeline
The build and deployment processes were automated using the CI server Jenkins.

![pytest]

The build was successfully automated with the below pipeline as a result. Jenkins was used as it offers a simple way to set up a continous integration and deployment environment for almost any combination of source code. Jenkins polls the VCS in this case github and the build is triggered by the github webhook when a change has been commited to a predetermined branch. In this project the webhook was configured to the master branch ensuring only project work that had been deemed as working was deployed.

![jenkins]



    



## Front End Design
Home page 
![home]
<br>
Main Library 
![library]
<br>
Create shelf page 
![create]
<br>
Update page 
![view]
<br>
Delete page
![delete]


#### Author
Joseph Igbinadolor


[usecase]: https://i.imgur.com/ssZejFD.png
[trello]: https://i.imgur.com/gDVtoEa.png
[docker]: https://i.imgur.com/T8sLaPo.png
[risk]: https://i.imgur.com/6wzviuE.png
[ierd]: https://i.imgur.com/3afg7oo.png
[ferd]: https://i.imgur.com/jVkdiBg.png
[pipeline]: https://i.imgur.com/749psqM.png
[jenkins]: https://i.imgur.com/xL8WbLt.png
[home]: https://i.imgur.com/qriaf17.png
[library]: https://i.imgur.com/ivahCWK.png
[create]: https://i.imgur.com/7NUpymd.png
[view]: https://i.imgur.com/wtKYt2o.png
[delete]: https://i.imgur.com/Rn5OF5X.png
[pytest]:https://i.imgur.com/749psqM.png
