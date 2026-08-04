from polymarket_bot.runtime.runner import RuntimeRunner


def test_runtime_without_engine():
    runner = RuntimeRunner()
    result = runner.handle_event({"price": 1})

    assert result.signal is None
    assert result.trade is None
