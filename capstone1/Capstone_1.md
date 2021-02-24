# Capstone 1: Kickstarter Projects
    I chose to do my exploratory data analysis on a collection of nearly 400,000 kickstarter projects. This dataset was fortunately quite clean already, but had a small handful of snags. There were a small number of null values, but some columns had values that were probably placeholders (like launch dates from the '70s). 

    Clean dataset, but mildly redundant
        Certain columns are just currency conversions
        of the null values
        Projects that started in 1970?!
        quantified state of projects -- mapped to dictionary
    
## Exploratory Data Analysis
    ![Descriptive Statistics](/images/ks_db_describe.png "Descriptive Statistics")
    While the data was generally applicable, I noticed that a few columns seemed redundant. The USD_ categories were presumably meant to convert currencies into a singular format for easier tabulation. However, a quick inspection revealed that currencies were already overwhelmingly USD anyway. 
    ![Normalized Currencies](/images/norm_cur.png "Normalized Currency Distribution"))
    
    Similarly, 


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