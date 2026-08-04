from polymarket_bot.monitoring.health import Health


if __name__ == "__main__":
    h = Health(True, True, True)
    print({"ready": h.ready})
