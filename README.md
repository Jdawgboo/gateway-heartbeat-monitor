# Gateway Heartbeat Monitor

Classify timestamped gateway heartbeat age as healthy, degraded, or stale using caller-provided thresholds.

```bash
cat heartbeats.json | python tool.py
python -m unittest -v
```

It is stateless and assumes timestamps share a unit. It does not poll gateways or send notifications.
