r
    model <- lm(final_score ~ attendance + assignment_grade, data=student_data)
    summary(model) # Views coefficients & model significance