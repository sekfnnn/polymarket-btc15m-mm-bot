# Architecture

## Components

- market: external data ingestion
- strategy: probability estimation
- execution: order decisions
- risk: capital protection
- backtest: historical simulation
- paper: forward simulation

## Trading flow

Data -> Features -> Probability -> Risk -> Quote -> Fill simulator

Live trading is disabled by default.
