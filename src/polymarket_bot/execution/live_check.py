def allow_live(config):
    return bool(config.get('live_trading', False))


def require_live_enabled(config):
    if not allow_live(config):
        raise RuntimeError('Live execution disabled')
