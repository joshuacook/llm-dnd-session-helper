import dataclasses
import yaml
import streamlit as st


@dataclasses.dataclass
class Campaign:
    campaign: str
    session: str

    def __post_init__(self):
        with open(f"campaigns/{self.campaign}/meta.yaml", "r") as campaign:
            self.campaign_data = yaml.safe_load(campaign)

        with open(f"campaigns/{self.campaign}/{self.session}.yaml", "r") as session:
            self.session_data = yaml.safe_load(session)

        self.data = self.campaign_data.copy()
        self.data.update(self.session_data)

    def st_edit_value(self, key: str, value: str = "", height: int = 100):
        st.subheader(key.capitalize())
        if key not in self.data.keys():
            self.data[key] = value
        edited = st.text_area(key, self.data[key], height=height)
        self.data[key] = edited
        self.save()

    def st_edit_list(self, key: str, height: int = 150):
        st.subheader(key.capitalize())
        values = self.data[key]
        edited = st.text_area(key, "\n".join(values), height=height)
        edited = edited.split("\n")
        self.data[key] = edited
        self.save()

    def st_edit_dict(self, key: str):
        st.subheader(key.capitalize())
        edited = st.data_editor(
            self.data[key],
            num_rows="dynamic",
            use_container_width=True,
        )
        self.data[key] = edited
        self.save()

    def save(self):
        for key in self.data.keys():
            if key in self.campaign_data.keys():
                self.campaign_data[key] = self.data[key]
            if key in self.session_data.keys():
                self.session_data[key] = self.data[key]
        with open(f"campaigns/{self.campaign}/{self.session}.yaml", "w") as session:
            yaml.dump(self.session_data, session)
        with open(f"campaigns/{self.campaign}/meta.yaml", "w") as campaign:
            yaml.dump(self.campaign_data, campaign)

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
