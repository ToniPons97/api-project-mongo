# api-project-mongo

- In this project I made a fictional public chat API using bottle for the HTTP server and MongoDB for the database.
- After having the api functioning properly I proceeded to make a simple sentiment analysis of the conversations and also    incorporated this into the api so that it does the analysis at runtime.
- to run the api first uncomment the code in the mongo_connect file and then comment it again so that it won't keep adding   the same information again and again.
- Then run the mongoapi.py file and it should start the server.
- The information that the api provides for the stored chats are well documented in the mongoapi.py file.
- The goal for the next time I revisit this project is to finish the recommender system based on words said and sentiments   of each user and to deploy the whole thing in Heroku.
- Hopefully you will enjoy this attempt!