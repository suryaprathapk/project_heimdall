#Project Heimdall
(tech_stack_eol_tracking)

This repo is for the project to scrape the web for End of Life time lines for various tech stacks used in Model N

## Back End
**Scrapy spiders for individual technologies**  

Spiders are divided into 2 stages
    
    1. Stage 1 performs a Google search and picks up the top link from the G Search results
        -- Outputs a JSON file with search results and page importance highlight 
    2. Second stage scrapper scrapes the link for the specific dates relate data
        -- Outputs a JSON file with EOL Dates

**Schedule**
    
1. Each scrapper is run by a single shell script in a fort-nightly or monthly cycle.
2. Plans to normalize the date formats is in progress


## Front End

1. Front is developed using Django web framework and Python.
2. Administrator has access to add and remove technologies
3. All the data is stored in sqllite db
4. Home page provides tile style web page with all the technologies listed by admin
5. Each tile has a view link that redirects to the individual technology's webpage with respective EOl timelines.







