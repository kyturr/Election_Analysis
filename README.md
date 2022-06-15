# Election_Analysis

## Overview of Election Audit
A Colorado Board of Elections employee has requested the following tasks for an audit of a local congressional election.
1. Total number of votes cast
2. A complete list of candidates who received votes
3. Total number of votes each candidate received
4. Percentage of votes each candidate won
5. The winner of the election based on popular vote

These results are to be obtained utilizing python to interpret and report on the data.

## Resources
* Data Source: election_results.csv
* Software: Python 3.10.4  Visual Studio Code, 1.67.2
## Election-Audit Results
The analysis of the election show that 
*There were 369,711 votes cast in the election
* The candidates were:
    * Charles Casper Stockham
    * Diana DeGette
    * Raymon Anthony Doane
* The candidate results were
    * Stockham received 23.0% of the vote and 85,213 votes
    * DeGette received 73.8% of the vote and 272,892 votes
    * Doane received 3.1% of the vote and 11,606 votes
* The winner of the election was
    * Diana De Gette who received 73.8% of the vote and 272,892 votes.
## Election-Audit Summary

The script as included may be used with any election data so long as the csv is in the same format of Ballot ID, County, Candidate. The script can be modified to vote on a measure or proposal as well by renaming the Candidate header to Yes/No and instead of candidate names marking yes or no in the CSV. This can be expanded on to include multiple measures and proposals but some minor additional code will need to be added. In practice, in the for row loop the “candidate_name” variable can be changed to prop1= row[2]. For each additional proposition: prop2=row[3], prop3=row[4], … etc. Just make sure each prop corresponds to the correct column, and each prop has its own votes variable to add.


![image](https://user-images.githubusercontent.com/103979048/173907190-d67b5459-11e2-4beb-9e2c-4a664a0641cd.png)
![image](https://user-images.githubusercontent.com/103979048/173907610-91c8e8df-f20b-40c7-818b-f8b8a1a3c4ca.png)


The script can also have a simple modification if used for an election that is nationwide to change county to state. This would be a simple variable replacement as well as script replacement in the prints.
