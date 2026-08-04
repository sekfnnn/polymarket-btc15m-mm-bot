# Polymarket BTC15m Market Maker Bot

Research-grade automated trading framework for BTC 15 minute prediction markets.

## Architecture

- Python 3.12 core
- async market data layer
- fee-aware probability engine
- maker-first execution
- queue-aware backtesting
- paper trading before live

## Safety

Live trading is disabled by default.

```yaml
LIVE_TRADING: false
```

## Development

```bash
pip install -e .[dev]
pytest
```
