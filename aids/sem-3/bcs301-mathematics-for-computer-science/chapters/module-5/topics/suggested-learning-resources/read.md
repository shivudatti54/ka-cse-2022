python
    from scipy import stats
    # Sample data: execution times for three algorithms
    algo_a = [2.1, 2.4, 1.9, 2.2]
    algo_b = [1.8, 2.0, 1.7, 1.9]
    algo_c = [3.1, 2.9, 3.3, 3.0]
    f_statistic, p_value = stats.f_oneway(algo_a, algo_b, algo_c)
    print(f"F-statistic: {f_statistic:.2f}, p-value: {p_value:.4f}")
    # A small p-value (e.g., < 0.05) suggests a significant difference.