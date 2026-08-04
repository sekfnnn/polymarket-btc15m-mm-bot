import pytest

from polymarket_bot.core.event_bus import EventBus

@pytest.mark.asyncio
async def test_event_bus_roundtrip():
    bus = EventBus()
    await bus.publish('event')
    assert await bus.consume() == 'event'
