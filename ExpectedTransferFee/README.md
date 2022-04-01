# Expected Transfer Fee across Big Five Leagues.

## This project will explore dominant factors to model transfer fees for players. By collecting skill data from football statistics pages along with transfer fee data from TransferMarkt provided by https://github.com/ewenme/transfers.



# Introduction

## How does the remaining length of the contract factor in to transfer price?
### The skill/athletical level of the football player is of course second to none. But a high length of a contract gives a club higher leveraging power due to player not being able to move freely without the clubs permission.

### The skill level is difficult to measure without enormous amounts of data. Expected goals, expected assists, percentage passes completed, dribbles completed is used to create a multivariate, linear model.


## How does the age factor into the transfer price? 
### A "fact" from the popular game Football Manager is that the prime age of a player is from the age 27 to 32. Here the player has accumulated large amount of experience while still having great athletical abilities. After a player has reached around 30 years old, the transfer fee for said player should then show a statiscial decay.

### After these steps are constructed, one should be able to create a VERY intuitive model for calculating the expected transfer fee. This is hypothesised taking the form of
<img src="https://render.githubusercontent.com/render/math?math=TF = SK (T-t) CV *exp(-age*\tau)"> $$
### where $TF$ is the transfer fee, $SK$ is the "skill value", $T$ is the date of contract expiry, $t$ is the current date, $CV$ is the "contract value" when the player last signed his contract and $\tau$ is the age factor, which ranges from $[0,1]$ with a bell shaped curve. 


# Method

## Workflow
### Data will be aquired by downloading the transfer dataset from https://github.com/ewenme/transfers, along with player data from footystats.org [https://footystats.org/download-stats-csv]. 

### This data will then be fed into a MySQL database. From there the data will be accessed into a python script/ jupyter notebook where analysis and deconstruction of the key factors will be presented. The final aim is then to compile the findings into a Tableu interactive chart for others to explore with. 

## Cleaning of data

### The transferdata contains alot of "loans" and therefore it may needs to be webscraped again. 

### The data will also not be uniform for the players, as some players will have much more datapoints as some players have played for more years. Additionally, some players have played in a non-top 5 league and will therefore not have any datapoints. A way to circumvent this is by doing an average of the last X games of players, or just look at the last completed season.

### The project which inspired me was a reddit post where a user tried to adjust signings from the 1992 to 2021 transfer window to show what the adjusted prices were. As the football sector have shown significant growth (and will continue to), prices have increased, most noteably by the Neymar transfer to Paris Saint Germain. The reddit post adjusted for inflation, 2.0% y/y, and a regression of the median transfer fee for each year of the dataset. This method will be incorporated here as to correctly give a clear picture of the transfer fees.




## Caveats
### How to proceed? To first know the skill level, one would have to have some "raw" data of the skill level to model it. The hypothesised model is a multiplicative one, instead of additive. It can therefore be made linear by doing a logarithmic transformation, which yields

$log(TK) = log(SK)+log(T-t)+log(CV)-age*\tau$

### I personally need to study this more as the time decay of the contract will annihilate the model approaching minus infinity. However if working with one year is equal to 1, one could circumvent this by assuming that if a contract is not signed for the last window that the contract will not be signed. That is if T-t reaches 0.5 expected TK = 0. But this assumption needs domain knowledge of how many contracts are renewed last 6 months. Another fix is just to use days or maybe months. Sounds much better.

### There should also be constraints on which effects are most interesting for each position. One interesting idea is to do backward selection on multivariate, linear regression of some key metrics for each position to induce what is the most important factor. (See figure sketches for ideas).

