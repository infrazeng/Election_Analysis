# Election Analysis

## Overview of Election Audit

The purpose of this project was to analyze the results of a Congressional election in Colorado by aggregating the votes from three counties: Jefferson, Arapahoe, and Denver. To achieve this, we utilized a Python program to analyze the election outcomes. The program calculated the total number of votes received by each candidate, determined the percentage of votes secured by each candidate, and identified the ultimate winner of the election. Furthermore, the program provided insights into the county with the highest voter turnout.

By running the Python program, we were able to obtain comprehensive and accurate information about the election results. The program's calculations enabled us to determine the total votes garnered by each candidate, allowing for a clear understanding of their respective performance. Additionally, the program's analysis revealed the percentage of votes secured by each candidate, offering insights into their level of popular support. Ultimately, the program identified the election's winner based on the highest vote count.

## Audit Results

• A total of 369,711 votes were cast in this election.

• County breakdown: Jefferson County recorded 38,855 votes, accounting for approximately 10.5% of the total votes. Denver County had the highest number of votes with 306,055, representing around 82.8% of the total. Arapahoe County registered 24,801 votes, constituting approximately 6.7% of the total votes cast.

• Denver County had the highest number of votes, with a total of 306,055 votes cast.

• Charles Casper Stockham received 85,213 votes, accounting for approximately 23.0% of the total votes. Diana DeGette received 272,892 votes, representing 73.8% of the total. Raymon Anthony Doane received 11,606 votes, making up 3.1% of the total votes cast.

• Diana DeGette emerged as the winner of the election, securing 272,892 votes, which is approximately 73.8% of the total vote.

![Results](/Resources/election_results.png)
![Analysis](/Resources/elction_analysis.png)

## Election-Audit Summary

This script has proven to be very helpful in determining the results of a small scale congressional election in Colorado. However, the winner of this election was determined by popular vote. Federal presidential elections, however, are not decided by a national popular vote, but by an electoral college. For these types of elections, various conditionals have to be added to the code, granting electoral points to a candidate only if they win a majority in a certain state. The winner would then be declared based on whether their number of electoral votes has crossed the 270 vote threshold. Additionally, the number of votes from each county in this election can be divided against the number of eligible voters in each county, thus determining the turnout rate for each location. This data could help the election commission determine which counties have higher voter turnouts.
