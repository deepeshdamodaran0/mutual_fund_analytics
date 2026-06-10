def recommend_funds(risk_level):

    recommendations = (
        perf[perf["risk_grade"] == risk_level]
        .sort_values("sharpe_ratio", ascending=False)
        [["scheme_name", "risk_grade", "sharpe_ratio"]]
        .head(3)
    )

    return recommendations

recommend_funds("Low")
recommend_funds("Moderate")
recommend_funds("High")
recommend_funds("Very High")