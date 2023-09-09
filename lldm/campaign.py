import dataclasses
import yaml


@dataclasses.dataclass
class Campaign:
    campaign: str
    session: str

    def __post_init__(self):
        with open(f"campaigns/{self.campaign}/meta.yaml", "r") as campaign:
            campaign_data = yaml.safe_load(campaign)

        with open(f"campaigns/{self.campaign}/{self.session}.yaml", "r") as session:
            session_data = yaml.safe_load(session)

        self.data = campaign_data.copy()
        self.data.update(session_data)

    def __repr__(self) -> str:
        print("CAMPAIGN")
        print(self.data["campaign"])
        print()
        print("ADVENTURE")
        print(self.data["adventure"])
        print()
        print("DM OBJECTIVES")
        for objective in self.data["dm_objectives"]:
            print(objective)
        print()
        print("PLAYER OBEJECTIVES")
        for objective in self.data["player_objectives"]:
            print(objective)

        return f"{self.campaign} {self.session}"
