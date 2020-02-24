# Book-Library WebApp
### Resources:
* Trello Board: https://trello.com/b/Ydgv39X2/sfia-project-book-library-webapp-joseph-i
* Website: http://35.189.67.154:5000/
* Presentation:https://docs.google.com/presentation/d/1grBFd1br-snfG0CajYf07WhpcW-0h-Orhmn1Vx1cwPA/edit#slide=id.g1f87997393_0_821
* Books data from kaggle: https://www.kaggle.com/meetnaren/goodreads-best-books
## Index
* [Scope & Objectives](#scope-&-objectives)
* [Deliverables](#deliverables)
* [Project Planning](#project-planning)
* [Risk Assessment](#risk-assessment)
* [Architecture](#architecture)
* [Deployment](#deployment)
* [Front End Design](#front-end-design)
* [Future improvements](#future-improvements)

## Scope & Objectives 
The overall objective of this project is to create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training. 


This includes the following aims:
* A Trello Board with full expansion on user stories, use cases and tasks 
* A relational Database with at least 2 tables in it and a modelled relationship 
* Documentation describing the architecture that will be used and a detailed Risk Assessment 
* Functional CRUD application created in Python 
* A documented TDD approach, fully designed test suites and automated tests for validation of the application
* A functioning front-end website and integrated API's using Flask
* Code fully integrated into a Version Control System using the Feature-Branch model which will subsequently be built through a CI server and deployed to a cloud-based virtual machine

## Deliverables
The CRUD web app being created to meet the project scope is a Book Library application. On the app, Users can navigate through a book database containing over six thousand books to find one they would be interested in reading. They will also be able to create personal shelves to which their favourite books in the app can be added or removed. 

In light of this, the minimum viable product for the app has been defined as the following- 
Users must be able to:
* Create a User account that stores:
  * *User First and Last Name*
  * *User Email*
  * *User Password*
* Login/Logout 
* View and update account details
* Create a personal shelf where books the user likes can be stored
* Add/Delete books from the personal shelf
* Alternatively log in as guest with the limitation of not being able to create a personal shelf

Additional functionalities to the Minimum Viable Product should include:
* Navigate through the book database and find details on books using the search bar
* View other users personal shelves
* Personal shelves could have a yearly lifetime

The project idea is illustrated in the below Use case diagram:
### Use Case Diagram
![usecase][usecase]

## Project planning
Trello, a project tracking tool, was used to both plan and track this project. The link to the trello board is in the resources above. 
![trello][trello]
The project outline and parameters were outlined as part of planning in the trello board to ensure the project remains on course throughout. The Tasks and Completed columns on the trello board were used as my tracking tools. 
## Risk Assessment
The Risk Assessment for this project utilises the Failure Modes and Effects Analysis (FMEA) Methodology often used in Reliability Engineering. An advantage of FMEA is that it allows quantitative analysis of the failure modes so corrective action can be used to address the most serious concerns.

In FMEA, the Risk Priority Number (RPN) = Severity x Occurrence x Detectibility. The aim is to get the RPN number as low as possible. 
The initial risk assessment was carried out during project planning and then updated throughout the project.
![risk]
The biggest risk was the potential of a CSRF attack however that was heavily mitigated by flasks in-built protection which detects when an instruction does not come from the user due to the lack of a secret key. 
HTTP traffic also forms a significant risk however, as this is a personal project that wont be used by the public mitigating this risk is not imperative. 
The remaining risks were classed as risks that can be lived with however, the assessment shows how they could be improved for future work and the effect it would have.
## Architecture

### Entity Relationship Diagram
The initial plan for the database structure is modelled below in the ERD. 

The database was intially modelled to have 3 tables in my ERD but whilst implementing this i concluded that to meet the project MVP aim of allowing users to create shelves, an extra table would be required.   
![ierd]

The final ERD as modelled below allows for the creation of shelves in the Shelf table and for the updating of shelves in the Book-shelf table with ShelfID creating a relationship between the two. The Many to One relationship between Users and Shelf means that each user can have multiple shelfs whilst the One to Many relationship between Shelf and Book-shelf means that for each shelf created, multiple books can be added.
![ferd] 


## Deployment

### CI Pipeline

The build and deployment processes were automated using the CI server Jenkins. Usually testing would also have been automated however due to issues with the pytest module in python and GCP, the testing process which was mapped out in the trello project plan was not carried out. Below is the planned CI pipeline. Filled in green are the steps that have been carried out for this project. 
![pipeline] 
Jenkins was used as it offers a simple way to set up a continous integration and deployment environment for almost any combination of source code. Jenkins polls the VCS in this case github and the build is triggered by the github webhook when a change has been commited to a predetermined branch. In this project the webhook was configured to the master branch ensuring only project work that had been deemed as working was deployed.    
Another advantage of using Jenkins for automated deployments is that Jenkins allows your app to be deployed as a background process. This frees up the instance for other work and ensures the application isnt accidentally shut down by closing the VM.

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

## Future improvements 
The main aims of this project were met with the exception of implementing a TDD approach. Therefore, the main future improvement for this project would be implementing a TDD approach and automated testing. 
Other improvements include:
* Use HTTPS protocol 
* Add functionality allowing user to view other users libraries

#### Author
Joseph Igbinadolor


[usecase]: https://i.imgur.com/ssZejFD.png
[trello]: https://i.imgur.com/gDVtoEa.png
[risk]: https://i.imgur.com/6wzviuE.png
[ierd]: https://i.imgur.com/3afg7oo.png
[ferd]: https://i.imgur.com/jVkdiBg.png
[pipeline]: https://i.imgur.com/749psqM.png
[home]: https://i.imgur.com/qriaf17.png
[library]: https://i.imgur.com/ivahCWK.png
[create]: https://i.imgur.com/7NUpymd.png
[view]: https://i.imgur.com/wtKYt2o.png
[delete]: https://i.imgur.com/Rn5OF5X.png
