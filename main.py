import glob
from lldm.campaign import Campaign
from lldm.prompter import Prompter
import streamlit as st
import pandas as pd

st.set_page_config(
    layout="wide",
)

sidebar = st.sidebar.title("Meta")
campaign_name = None
session_name = None
campaign = None

campaigns = glob.glob("campaigns/*")
campaigns = [campaign.split("/")[-1] for campaign in campaigns]
campaign_name = st.sidebar.selectbox("Campaign Name", campaigns, index=2)

if campaign_name:
    sessions = glob.glob(f"campaigns/{campaign_name}/*.yaml")
    sessions = [session.split("/")[-1].split(".")[0] for session in sessions]
    sessions = [session for session in sessions if session != "meta"]
    session_name = st.sidebar.selectbox("Session Name", sessions)

if session_name:
    campaign = Campaign(
        campaign=campaign_name,
        session=session_name,
    )


recap_tab, campaign_tab, session_tab, players_tab, scene_gen_tab = st.tabs(
    ["Recap", "Campaign", "Session", "Players", "Scene Generator"]
)

with recap_tab:
    if campaign:
        if st.button("Generate Recap"):
            recapper = Prompter(
                gpt4=True,
                data=campaign.data,
                kinds=[
                    "recap",
                    "campaign",
                    "session",
                ],
            )
            recap = recapper.chat()
            campaign.data["recap"] = recap
            campaign.save()
        else:
            recap = campaign.data["recap"]
        campaign.st_edit_value("recap", recap, height=450)

with players_tab:
    if campaign:
        campaign.st_edit_dict("players")

with campaign_tab:
    if campaign:
        campaign.st_edit_value("campaign")
        campaign.st_edit_list("dm_objectives")

with session_tab:
    if campaign:
        campaign.st_edit_value("adventure")
        campaign.st_edit_list("player_objectives")
        campaign.st_edit_dict("scenes")
        campaign.st_edit_dict("locations")
        campaign.st_edit_dict("npcs")

with scene_gen_tab:
    scenes = campaign.data["scenes"]
    current_scene = scenes[-1]
    st.write(current_scene)