

# DIY webscraper --------------------------------------------------------------

source("src/packages.R")
# get league metadata

league_meta <- read_csv("config/league-meta.csv")


league_name <- league_meta$league_name[1]
league_id <- league_meta$league_id[1]
season_id <- 2020

# Get URL

summer_transfers_url <- glue(
  "https://www.transfermarkt.com/{league_name}/transfers/wettbewerb/{league_id}/plus/?saison_id={season_id}&s_w=s"
)
winter_transfers_url <- glue(
  "https://www.transfermarkt.com/{league_name}/transfers/wettbewerb/{league_id}/plus/?saison_id={season_id}&s_w=w"
)

# read page
summer_transfers_page <- read_html(summer_transfers_url)
winter_transfers_page <- read_html(winter_transfers_url)



page <- summer_transfers_page 

clubs <- page %>%
  html_elements('.table_header') %>%
  html_text2() 








# get transfers data
summer_transfers <- extract_transfers(summer_transfers_page, window = "Summer")
winter_transfers <- extract_transfers(winter_transfers_page, window = "Winter")

# merge 
transfers <- bind_rows(summer_transfers, winter_transfers)
