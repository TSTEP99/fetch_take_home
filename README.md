# fetch_take_home
Take Home Assignment for Fetch

This github repo is written using python3

This code requires the use of psycopg2

This can installed with the following line of code:

```
pip install psycopg2-binary
```

The code can be run  using the following
```
python take_home.py
```

Questions:

1.
Credentials: In the example code, I've used hardcoded credentials to access the SQS queue and the Postgres database. In a production environment, you should use a more secure way to store and manage these credentials.
Scaling: he example code uses a simple while loop to read messages from the SQS queue. In a production environment, you would need to handle a much larger number of messages, so you would need to use a more scalable approach.
Error handling: The example code doesn't include any error handling. In a production environment, you would need to handle errors and exceptions gracefully, such as retrying failed operations or logging error messages.
Monitoring: The example code doesn't include any monitoring or logging. In a production environment, you would need to monitor the performance of the system and log any important events to help with troubleshooting and debugging.
Security : The example code is only an example and doesn't include any security features. In a production environment, you would need to secure the data in transit and at rest.

2.
In addition to the answer above, a few other things I might add are test cases to ensure the code works in different scenarios, and possible retries to handle different exceptions and failures as well as more documentation to make the code more readable.

3.
You could use something like AWS Lambda  to run the code in a scalable way.

4.
I used a fairly simple encryption scheme that would not be too difficult to reversse. However, I could use a hashing function that is invertible in he future however, I lacked the time to code this.

5.I assumed that the app version only wanted the first digit of the app version given from the queue since the field was a integer in the table.Another possible error I made was not deleting messages off of the queue and is something I could take care of in the future but I assumped this was not necessary.





