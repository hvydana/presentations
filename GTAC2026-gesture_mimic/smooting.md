```python
# ── action smoothing ──────────────────────────────────────────────────────
def smooth_actions(actions, window=1, method="mean"):
    """Apply causal smoothing to a (T, D) array of predicted actions.

    method:
      - "mean": causal moving average over the last `window` frames.
      - "ema":  exponential moving average with alpha = 2/(window+1).

    Returns the smoothed array (same shape, same dtype as input).
    """
    if window is None or window <= 1:
        return actions
    a = np.asarray(actions, dtype=np.float64)
    if a.ndim == 1:
        a = a[:, None]
    T = a.shape[0]
    out = np.empty_like(a)

    if method == "ema":
        alpha = 2.0 / (window + 1.0)
        out[0] = a[0]
        for t in range(1, T):
            out[t] = alpha * a[t] + (1.0 - alpha) * out[t - 1]
    else:
        # Causal moving average (uses min(window, t+1) samples at the start).
        csum = np.cumsum(a, axis=0)
        for t in range(T):
            w = min(window, t + 1)
            s = csum[t] - (csum[t - w] if t - w >= 0 else 0.0)
            out[t] = s / w

    if actions.ndim == 1:
        out = out[:, 0]
    return out.astype(np.asarray(actions).dtype)
```