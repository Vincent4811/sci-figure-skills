"""SIMULATED food-microbiology data for templates only. NOT real measurements."""
import numpy as np, pandas as pd
rng = np.random.default_rng(42)

def growth():
    # Modified Gompertz (Zwietering 1990), log10 CFU/mL vs time, 3 temperatures, 3 reps
    t = np.arange(0, 49, 3.0); rows = []
    for temp, mu, lag in [(10, .15, 12), (25, .45, 4), (37, .7, 2)]:
        N0, A = 3.0, 6.0
        y = N0 + A*np.exp(-np.exp(mu*np.e/A*(lag - t) + 1))
        for r in range(3):
            for ti, yi in zip(t, y + rng.normal(0, .12, t.size)):
                rows.append(dict(temp_C=temp, rep=r+1, time_h=ti, log_cfu=yi))
    return pd.DataFrame(rows)

def survival():
    # Log-linear inactivation: log N = log N0 - t/D at 3 temperatures
    rows = []
    for temp, D in [(55, 8.0), (60, 2.5), (65, .8)]:
        tmax = 5*D
        for r in range(3):
            for ti in np.linspace(0, tmax, 7):
                rows.append(dict(temp_C=temp, rep=r+1, time_min=ti, log_cfu=7 - ti/D + rng.normal(0, .15)))
    return pd.DataFrame(rows)

def cfu():
    rows = []
    for trt, m in [("Control", 6.2), ("Washed", 5.1), ("Washed+PAA", 3.4), ("UV-C", 4.3)]:
        for v in rng.normal(m, .45, 8): rows.append(dict(treatment=trt, log_cfu_g=v))
    return pd.DataFrame(rows)

if __name__ == "__main__":
    import os; os.makedirs("../examples/data", exist_ok=True)
    growth().to_csv("../examples/data/sim_growth.csv", index=False)
    survival().to_csv("../examples/data/sim_survival.csv", index=False)
    cfu().to_csv("../examples/data/sim_cfu.csv", index=False)
