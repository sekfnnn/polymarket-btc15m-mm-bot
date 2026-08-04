from polymarket_bot.monitoring.health import Health


def test_health_ready():
    h = Health()
    assert h.ready()


def test_health_not_ready_when_disabled():
    h = Health()
    h.oracle_ok = False
    assert not h.ready()
