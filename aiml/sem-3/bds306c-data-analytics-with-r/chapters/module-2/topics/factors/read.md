r
# Creating a simple factor from a character vector
department <- c("CSE", "ECE", "ME", "CSE", "CIVIL", "ECE")
department_factor <- factor(department)

print(department_factor)
# Output: [1] CSE   ECE   ME    CSE   CIVIL ECE
#          Levels: CIVIL CSE ECE ME

# Check the structure
str(department_factor)
# Output: Factor w/ 4 levels "CIVIL","CSE",..: 2 3 4 2 1 3