r
    # Example of data wrangling with dplyr
    library(dplyr)
    clean_data <- raw_data %>%
      filter(!is.na(column_name)) %>%        # Remove rows with NA
      mutate(new_column = old_column * 2) %>% # Create new column
      select(-irrelevant_column) %>%          # Remove a column
      rename(new_name = old_name)             # Rename a column