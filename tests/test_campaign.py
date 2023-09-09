from lldm.campaign import Campaign


def test_campaign_repr():
    # Create a Campaign object
    campaign = Campaign(campaign="test", session="test")

    assert set(campaign.data.keys()) == set(
        [
            "adventure",
            "campaign",
            "party",
            "players",
            "dm_objectives",
            "locations",
            "npcs",
            "player_objectives",
            "scenes",
        ]
    )
    assert str(campaign) == "test test"
