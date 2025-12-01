import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def generate_synthetic_customer_data(n_customers: int = 1000, random_state: int = 42) -> pd.DataFrame:
    """
    Generate realistic synthetic customer engagement data for a retail context.
    """

    rng = np.random.default_rng(random_state)

    # Latent engagement factor (higher = more engaged customer)
    engagement_factor = rng.normal(loc=0.0, scale=1.0, size=n_customers)

    # Core behavioral metrics (monthly-ish)
    visits_per_month = np.clip(
        4 + 2.0 * engagement_factor + rng.normal(0, 1.5, n_customers),
        a_min=0,
        a_max=None,
    )

    avg_session_duration_min = np.clip(
        5 + 3.0 * engagement_factor + rng.normal(0, 2.0, n_customers),
        a_min=1,
        a_max=None,
    )

    pages_per_session = np.clip(
        3 + 1.5 * engagement_factor + rng.normal(0, 1.0, n_customers),
        a_min=1,
        a_max=None,
    )

    # Marketing engagement
    email_open_rate = np.clip(
        0.15 + 0.1 * engagement_factor + rng.normal(0, 0.05, n_customers),
        a_min=0,
        a_max=1,
    )

    email_click_through_rate = np.clip(
        0.03 + 0.07 * engagement_factor + rng.normal(0, 0.03, n_customers),
        a_min=0,
        a_max=1,
    )

    # Conversion & value
    purchase_frequency_per_month = np.clip(
        0.5 + 0.6 * engagement_factor + rng.normal(0, 0.3, n_customers),
        a_min=0,
        a_max=None,
    )

    avg_order_value = np.clip(
        40 + 8.0 * engagement_factor + rng.normal(0, 10, n_customers),
        a_min=5,
        a_max=None,
    )

    customer_lifetime_value = np.clip(
        200 + 80 * engagement_factor
        + 10 * purchase_frequency_per_month
        + 0.5 * avg_order_value
        + rng.normal(0, 50, n_customers),
        a_min=0,
        a_max=None,
    )

    nps_score = np.clip(
        20 + 15 * engagement_factor + rng.normal(0, 10, n_customers),
        a_min=-100,
        a_max=100,
    )

    df = pd.DataFrame(
        {
            "Visits per Month": visits_per_month,
            "Avg Session Duration (min)": avg_session_duration_min,
            "Pages per Session": pages_per_session,
            "Email Open Rate": email_open_rate,
            "Email CTR": email_click_through_rate,
            "Purchase Frequency / Month": purchase_frequency_per_month,
            "Average Order Value ($)": avg_order_value,
            "Customer Lifetime Value ($)": customer_lifetime_value,
            "NPS Score": nps_score,
        }
    )

    return df


def main():
    # --- Data preparation ---
    df = generate_synthetic_customer_data()

    # --- Correlation matrix ---
    corr = df.corr()

    # --- Seaborn styling for executive / board-level presentation ---
    sns.set_style("white")
    sns.set_context("talk")  # presentation-ready text sizes

    # --- Create 512x512 canvas ---
    # Create the figure with an explicit DPI so the canvas is exactly
    # 8 inches * 64 dpi = 512 pixels. We'll create the figure with
    # `dpi=64` and `figsize=(8, 8)` and save using the figure's DPI
    # without using `bbox_inches='tight'` (which can crop and change
    # the final pixel dimensions).
    fig, ax = plt.subplots(figsize=(8, 8), dpi=64)

    # Mask upper triangle for cleaner presentation
    mask = np.triu(np.ones_like(corr, dtype=bool))

    ax = sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".2f",
        cmap="YlGnBu",
        vmin=-1,
        vmax=1,
        linewidths=0.5,
        square=True,
        cbar_kws={
            "shrink": 0.8,
            "label": "Pearson Correlation",
        },
        ax=ax,
    )

    # Titles & labels tuned for an executive audience
    ax.set_title(
        "Customer Engagement Metric Correlation Matrix",
        pad=20,
        fontsize=18,
        weight="bold",
    )
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
    ax.set_yticklabels(ax.get_yticklabels(), rotation=0)

    # Do not call `plt.tight_layout()` or save with `bbox_inches='tight'`.
    # Those can change the final pixel dimensions by trimming whitespace.
    # Instead save using the figure's DPI so `figsize * dpi` yields exact pixels.
    fig.savefig("chart.png", dpi=fig.dpi)
    plt.close(fig)


if __name__ == "__main__":
    main()
