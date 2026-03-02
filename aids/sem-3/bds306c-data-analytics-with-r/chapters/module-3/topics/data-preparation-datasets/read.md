r
# Load the tidyverse
library(tidyverse)

# Read a CSV file
my_data <- read_csv("path/to/your/dataset.csv")

# Read a TXT file with tab separator
my_data <- read_delim("data.txt", delim = "\t")