AUCTION BIDDING SYSTEM
     
    This project has been completed with python as the programming language for the application and firebase
    for database purpose.
    OVERVIEW :an auction bidding application which takes and stores  the number of users interested in bidding provides them an user id also asks them their username for the purpose of post bidding result display . It has been added with a table of item selection for bidding, each with their own starting price.
    The application has an inbuilt timer to check starting time and end time of the bid. The program has been connected with firebase through JSON files      which are automatically created when it detects there is no JSON file in the folder/directory 
    

Future Prospects:
- Change the Code to Make an Actual Useable Auction System
- Add a UI and More Security so that the Database isn't Corrupted from External Intruders

Flaws:
- Integrating the JSON file had Certain Advantages like Creating the Accurate JSON File in case it doesn't Exist but it is Also a Security Flaw which would Allow External Intruders to get Access to the Database (CURRENTLY)

Strengths:
- Can be Accessed from Almost Anywhere since the Database is Hosted Online on a NoSQL Database FIREBASE

Firebase workaround :
Instead of localised sql database firebase can be an effective alternative as it has many multipurpose 
tools like authentication, machine learning, hosting and 2 types of malleable databases etc.

In this case we have used python integrations of firestore to do CRUD operations and store input data.
Since firebase is owned by google it has pretty good security measures and scalable storage capabilities with pay as you go system after initial free trial.

HOW TO RUN ?
Installation of python is must .
User needs to install firebase-admin python library and change the filepath of the JSON file .

HOW TO ACCESS THE DATA AND RESULTS:
Access the firebase firestore database https://console.firebase.google.com/u/0/project/auction-bidding-arjun-gupta/firestore/data/~2FBid

login credentials : 

user id - viewerdome@gmail.com
 
 password - 12345$$12345





