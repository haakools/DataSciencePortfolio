# StatsBombR ------------------------------------------------------------------

install.packages("devtools")
install.packages("remotes")
remotes::install_version("SDMTools", "1.1-221")
devtools::install_github("statsbomb/StatsBombR")

library(tidyverse)
library(StatsBombR) #1

Comp <- FreeCompetitions() %>%
  filter(competition_id==11 & season_name=="2005/2006") #2

Matches <- FreeMatches(Comp) #3

StatsBombData <- StatsBombFreeEvents(MatchesDF = Matches, Parallel = T) #4

StatsBombData = allclean(StatsBombData) #5