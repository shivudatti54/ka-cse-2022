r
# A simple character vector
departments <- c("CSE", "ECE", "Mech", "CSE", "Civil", "ECE")
print(departments)
# [1] "CSE"   "ECE"   "Mech"  "CSE"   "Civil" "ECE"

# Converting it to a factor
dept_factor <- factor(departments)
print(dept_factor)
# [1] CSE   ECE   Mech  CSE   Civil ECE
# Levels: Civil CSE ECE Mech