# Election Analysis

## Overview of Election Audit

The purpose of this project was to analyze the results of a Congressional eleciton in Colorado by tallying up the votes from three counties: Jefferson, Arapahoe, and Denver. The Python program that we will use to analyze the results of the election will calculate the total number of votes won by each candidate, the percentage of votes won by each candidate, and who is the winner of the election. Additionally, this program will let us know which county had the highest turnout. 

## Election-Audit Results

• 369,711 votes were cast in this election
• Breakdown by county: there were 38,855 votes cast in Jefferson County, about 10.5% of the total votes cast, 306,055 votes cast in Denver County, about 82.8%, and 24,801 votes cast in Arapahoe county, about 6.7% of the total votes cast
• Denver county had by far the highest number of votes with 305,055 votes cast.
• Charles Casper Stockham receives 85,213 votes, about 23.0% of the total, Diana DeGette receives 272,892 votes, 73.8% of the total, and Raymon Anthony Doane received 11,606 votes, 3.1% of the total.
• Diana DeGette won the election with 272,892 votes, about 73.8% of the total vote.

## Election-Audit Summary

This script has proven to be very helpful in determining the results of a small scale congressional election in Colorado. However, the winner of this election was determined by popular vote. Federal presidential elections, however, are not decided by a national popular vote, but by an electoral college. For these types of elections, various conditionals have to be added to the code, granting electoral points to a candidate only if they win a majority in a certain state. The winner would then be declared based on whether their number of electoral votes has crossed the 270 vote threshold. Additionally, the number of votes from each county in this election can be divided against the number of eligible voters in each county, thus determining the turnout rate for each location. This data could help the election commission determine which counties have higher voter turnouts.
