from pathlib import Path


def validate_tree():
    required = [
        'src/polymarket_bot',
        'tests',
        'config'
    ]
    return all(Path(x).exists() for x in required)


if __name__ == '__main__':
    print('ok' if validate_tree() else 'missing files')
