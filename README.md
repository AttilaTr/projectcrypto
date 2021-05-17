Detailed readme in projectcrypto.docx

Project Crypto

Concept

The main goal of this project is to create a database accessible online, in which users can add, and delete articles on a graphical interface about cryptocurrencies they are interested in. 

Specification

To fulfil the goal specified in the concept, the following methods and technologies have been used:

Project management

For creating and tracking the development of the project Trello’s Kanban board has been used. It contains user stories and the colour coded MOSCOW prioritisation of the elements from day 1 to the last day of coding.



Version control

To be able to follow the advancement of coding I applied GITHUB as a version control application. I created branches for each days of coding to be able to compare and if necessary, revert the different versions of coding. The name of the repository is “projectcrypto”.



Databases

The current design of the databases is the following using ERD (Entity Relationship Diagram).
There are two tables: Cryptocurrencies and Articles. They are connected by one to many relationship as one cryptocurrency can be present in many articles.
I created the actual database in Flask application, using Python as a programming language.





Risk assessment


A created a risk assessment to be able to realize and mitigate the possible risks during the project.




CI pipeline

I decided to use Jenkins as a CI server and I built automated testing of the current code inside Jenkins, which generates a report of the tested codes.



I tested the actual code and received the following result:


The Design

The final design was done by using basic HTML coding and a Python application called Flask.



