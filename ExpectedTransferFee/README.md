# Expected Transfer Fee across Big Five Leagues.

## This project will explore dominant factors to model transfer fees for players. By collecting skill data from football statistics pages along with transfer fee data from TransferMarkt provided by https://github.com/ewenme/transfers.



# Introduction

## How does the remaining length of the contract factor in to transfer price?
### The skill/athletical level of the football player is of course second to none. But a high length of a contract gives a club higher leveraging power due to player not being able to move freely without the clubs permission.

### The skill level is difficult to measure without enormous amounts of data. Expected goals, expected assists, percentage passes completed, dribbles completed is used to create a multivariate, linear model.


## How does the age factor into the transfer price? 
### A "fact" from the popular game Football Manager is that the prime age of a player is from the age 27 to 32. Here the player has accumulated large amount of experience while still having great athletical abilities. After a player has reached around 30 years old, the transfer fee for said player should then show a statiscial decay.

### After these steps are constructed, one should be able to create a VERY intuitive model for calculating the expected transfer fee. This is hypothesised taking the form of
 $TF = SK (T-t) CV *\tau$
### where $TF$ is the transfer fee, $SK$ is the "skill value", $T$ is the date of contract expiry, $t$ is the current date, $CV$ is the "contract value" when the player last signed his contract and $\tau$ is the age factor, which ranges from $[0,1]$ with a bell shaped curve. 


# Method

## Workflow
### Data will be aquired by downloading the transfer dataset from https://github.com/ewenme/transfers, along with player data from footystats.org [https://footystats.org/download-stats-csv]. 

### This data will then be fed into a MySQL database. From there the data will be accessed into a python script/ jupyter notebook where analysis and deconstruction of the key factors will be correlated.

## Cleaning of data

## Caveats
### How to proceed? To first know the skill level, one would have to have some "raw" data of the skill level to modell it. 



