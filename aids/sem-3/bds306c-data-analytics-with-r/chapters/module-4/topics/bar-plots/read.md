r
    # Creates a bar plot of counts for each category in 'category_column'
    ggplot(data, aes(x = category_column)) + geom_bar()