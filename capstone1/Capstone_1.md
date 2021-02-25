# Capstone 1: Kickstarter Projects
I chose to do my exploratory data analysis on a collection of nearly 400,000 kickstarter projects. Columns included project start/completion date, status, and backer and pledge counts.This dataset was fortunately quite clean already, but had a small handful of snags. There were a small number of null values, but some columns had values that were probably placeholders (like launch dates from the '70s). I tried to find these projects on kickstarter for clues about this using their search function on name and ID, but ultimately came up empty-handed. 

    
## Exploratory Data Analysis
![Descriptive Statistics](/images/ks_db_describe.png "Descriptive Statistics")
While the data was generally applicable, I noticed that a few columns seemed redundant. The 'USD_' categories were presumably meant to convert currencies into a singular format for easier tabulation. However, a quick inspection revealed that currencies were already overwhelmingly USD anyway. 

![Normalized Currencies](/images/norm_cur.png "Normalized Currency Distribution")
    
Similarly, when I looked into Kickstarter's policies, pledges are always collected in the project's native currency. I double-checked this by trying to identify any rows with a currency that didn't match its country (e.g. USD:US, GBP:GB). This means we can infer where projects originated by their currency used. 

Given the proportion of USD projects, the outdated conversion rates, and that USD covered both extremes (min/max) I elected to leave out the converted values and work with the raw amounts. 

Next, I saw that the 'length' column I calculated using 'launched' and 'pledged' had some incredibly large values! For whatever reason, a handful of projects had a launch date of 1970-01-01. I decided the safest choice was to change these to Kickstarter's official launch date of 2009-04-28.

Moving into the bulk of the data, the Seaborn library had some readily available tools for representing categorical data -- namely, it gave easily digestible breakdowns of the sub-categories, e.g. genres in Film & Video. 
![Film & Video Genres](/images/Film&Video.png "Film & Video category breakdown")

The remaining images are stored in the [/images folder](/images) to save space. 

While it is self-explanatory that projects without *any* backers would be failed or cancelled, the concentration of small goal amounts, backer counts, and pledges against the extreme outliers made the scale difficult to present

        breakdown of subcategory per category
        normalized distribution of success/failures per category
    What category is most successful?
    Does a category make more on average than others?
    While the number of backers is predictably indicative of pledge *totals*, neither of these bore a strong relation to a project's success
        
## Hypothesis Tests
    Projects in more popular categories are more likely to succeed

### Sampling Comparisons
    Take bootstrapped mean of most popular category (Film & Video). T-test this value against all other means, to determine its likelihood of success.

## Future Ideas
    Observe relationship of pledges through lifetime of a project
    Where do the pledges come from? 

vocabulary of a statistical test