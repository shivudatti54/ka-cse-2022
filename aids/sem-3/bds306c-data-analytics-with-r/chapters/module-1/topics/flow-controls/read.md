r
    # Example: Categorizing a test score
    score <- 85

    if (score >= 90) {
      grade <- "A"
    } else if (score >= 80) {
      grade <- "B"  # This will execute for score = 85
    } else if (score >= 70) {
      grade <- "C"
    } else {
      grade <- "F"
    }
    print(grade)
    # Output: [1] "B"