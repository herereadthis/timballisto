import pytest
from bunco import Player


@pytest.fixture
def response():
    """Test fixture."""
    import requests
    return requests.get('https://github.com/herereadthis/lutra.git')


def test_roll():
    player = Player()
    player.roll()
    assert len(player.get_dice) == player.dice_count
