"""Initial Table Population

Revision ID: a795e83fe4a8
Revises: 44b4398d8366
Create Date: 2023-09-10 21:17:34.072821

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
from lldm.models import (
    Adventure,
    Campaign,
    Character,
    GameSession,
    Location,
    NPC,
    Objective,
    Scene,
)


# revision identifiers, used by Alembic.
revision: str = 'a795e83fe4a8'
down_revision: Union[str, None] = '44b4398d8366'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    bind = op.get_bind()
    engine = sqlmodel.create_engine("sqlite:///lldm.db")
    sqlmodel.SQLModel.metadata.create_all(engine)

    with sqlmodel.Session(engine) as session:
        campaign_os_chultanhos = Campaign(
            name="The Fey Wastes",
            description="In the desolate Fey Wastes, desert tribe members embark on a quest to rescue a kidnapped brother after the destruction of their camp and annihilation of their people by a gang of Minotaurs. Joined by two amnesiac Eladrin who recently wandered out of the desert, the party ventures deeper into the mysteries of this barren land.",
            party="Os Chultanhos",
        )
        session.add(campaign_os_chultanhos)
        session.commit()
        session.refresh(campaign_os_chultanhos)
        objective_1 = Objective(
            name="Discover the truth about what happened to the Fey Wild.",
            description="Discover the truth about what happened to the Fey Wild.",
            campaign_id=campaign_os_chultanhos.id,
            hidden=True,
            term="long",
            owner="gm",
        )
        session.add(objective_1)
        objective_2 = Objective(
            name="Discover the truth about what happened to the Seelie Court.",
            description="Discover the truth about what happened to the Seelie Court.",
            campaign_id=campaign_os_chultanhos.id,
            hidden=True,
            term="long",
            owner="gm",
        )
        session.add(objective_2)
        objective_3 = Objective(
            name="Find their brother, Bero, who is currently held captive in a secret area of Hanta's compound.",
            description="Find their brother, Bero, who is currently held captive in a secret area of Hanta's compound.",
            campaign_id=campaign_os_chultanhos.id,
            hidden=False,
            term="short",
            owner="gm",
        )
        session.add(objective_3)
        objective_4 = Objective(
            name="Prevent the Marquis from discovering the truth about Bero.",
            description="Prevent the Marquis from discovering the truth about Bero.",
            campaign_id=campaign_os_chultanhos.id,
            hidden=False,
            term="short",
            owner="gm",
        )
        session.add(objective_4)
        character_1 = Character(
            name="Haemon",
            description="A bedouin from the deserts of the Fey Wastes who is intent on helping his brother that may actually be the reincarnation of Oberon; Has traveled over much of the Fey Wastes; Spore Druid",
            campaign_id=campaign_os_chultanhos.id,
            character_class="Druid",
            secrets=None,
        )
        session.add(character_1)
        character_2 = Character(
            name="Oggvay",
            description="A bedouin from the deserts of the Fey Wastes who is intent on helping his brother that may actually be the reincarnation of Oberon",
            campaign_id=campaign_os_chultanhos.id,
            character_class="Barbarian",
            secrets=None,
        )
        session.add(character_2)
        character_3 = Character(
            name="Spat",
            description="an amnesiac Eladrin",
            campaign_id=campaign_os_chultanhos.id,
            character_class="Wizard",
            secrets="guard from the destroyed Seelie Court",
        )
        session.add(character_3)
        character_4 = Character(
            name="Dev",
            description="an amnesiac Eladrin",
            campaign_id=campaign_os_chultanhos.id,
            character_class="Monk",
            secrets="guard from the destroyed Seelie Court",
        )
        session.add(character_4)
        location_1 = Location(
            name="Bodat",
            description="a city in the middle of the desert, run by Minotaurs, ruled by the Marquis",
            campaign_id=campaign_os_chultanhos.id,
        )
        session.add(location_1)
        location_2 = Location(
            name="Hanta's compound",
            description="a compound run by Hanta, a human who runs the human slave trade in Bodat, may have Haemon and Oggvay's brother, Bero",
            campaign_id=campaign_os_chultanhos.id,
        )
        session.add(location_2)
        location_3 = Location(
            name="the Kobold District",
            description="a district of Bodat where kobolds are not completely oppressed",
            campaign_id=campaign_os_chultanhos.id,
        )
        session.add(location_3)
        location_4 = Location(
            name="the hotel",
            description="human-friendly, players have a room here, run by weak old minotaur, secret passage to the whispering basin",
            campaign_id=campaign_os_chultanhos.id,
        )
        session.add(location_4)
        location_5 = Location(
            name="the whispering basin",
            description="a human-friendly tavern, mostly not entirely unsavory humans, some kobolds",
            campaign_id=campaign_os_chultanhos.id,
        )
        session.add(location_5)
        npc_1 = NPC(
            name="Hanta",
            description="human, runs the human slave trade in Bodat, has Bero",
            campaign_id=campaign_os_chultanhos.id,
        )
        session.add(npc_1)
        game_session_1 = GameSession(
            name="20230911",
            campaign_id=campaign_os_chultanhos.id,
            description="""
            Our party, in the midst of their mission to rescue Bero, their kidnapped kin,
    from the clutches of human slave trader Hanta, remained nestled in the minotaur-dominated
    town of Bodat. Governed by the enigmatic Marquis, Bodat presented treacherous terrain
    for our fearless adventurers, Haemon, Oggvay, Spat, and Dev, who found themselves
    playing a dangerous game of evasion against both Minotaurs police force and Hanta''s
    Minotaur thugs. With a personal vendetta against those who destroyed their desert
    camp and an enigmatic directive from a coyote to learn to fly, their journey is
    far from over.


    Our crew found themselves lurking near the Whispering Basin, on the verge of making
    an entrance into the shrouded Kobold District. However, they chose instead to keep
    company with a local group of felines who claimed they knew a thing or two about
    navigating the tunnels in Bodat. The sly cats hinted at a shadowy figure known as
    the ''Prince of all Cats,'' who commands the ears of the Minotaur townsmen. Later,
    after maneuvering their way into Hanta''s compound successfully, our group stumbled
    upon a note, ''camp destroyed; child recovered.'' Once again, the grim reminder
    of the brutal attack they had survived, and the loss of their brother Bero echoed
    in their minds, fueling their resolve to confront the tormentors.


    Peeling back layers of mystery, our party''s exploration  inadvertently triggered
    a Shujusreckus jukebox in the dining area. The sudden cacophony sent them scampering
    across the compound, stealth no longer an option. As they sprinted desperately towards
    the vicinity of the slave pens, they inadvertently crossed paths with a Minotaur,
    leaving them in the awkward radius of his immediate attention. Will our adventurers
    manage to weather this storm stirred by their own hands? Only time will tell.
            """
        )
        session.add(game_session_1)
        session.commit()
        session.refresh(game_session_1)
        adventure_1 = Adventure(
            name="Bodat",
            description="In the minotaur-populated town of Bodat, governed by the enigmatic Marquis, the adventurers must avoid capture by the Minotaur police force while they search for their kidnapped brother, Bero, who may or may not be the reincarnation of the fallen god, Oberon.",
            campaign_id=campaign_os_chultanhos.id,
        ) 
        session.add(adventure_1)
        scene_1 = Scene(
            name="the cats",
            description="while lurking near the Whispering Basin and thinking about entering the Kobold District, they hung out with some cats. They know the tunnels in Bodat a little bit. The man in the palace is the ''Prince of all Cats'', smells like a cat but darker; the minotaurs listen to him",
            campaign_id=campaign_os_chultanhos.id,
            session_id=game_session_1.id,
            kind="interaction",
            location_id=location_3.id,
            outcome="good"
        )
        session.add(scene_1)
        scene_2 = Scene(
            name="sneaking into Hanta's part 2",
            description="succesfully snuck into Hanta''s compound, found a note that said ''camp destroyed; child recovered''; here ''camp'' most likely describes the attack suffered a few weeks ago when Bero was kidnapped and their whole village was slaughtered",
            campaign_id=campaign_os_chultanhos.id,
            session_id=game_session_1.id,
            kind="obstacle",
            location_id=location_2.id,
            outcome="good",
            previous_scene_id=scene_1.id
        )
        session.add(scene_2)
        scene_3 = Scene(
            name="the dining room",
            description="Accidentally set off a Shujusreckus jukebox which made a ton of noise in the dining room. We ran through the compound to near the slave pens, and accidentally ran into a minotaur.",
            campaign_id=campaign_os_chultanhos.id,
            session_id=game_session_1.id,
            kind="interaction",
            location_id=location_2.id,
            outcome="bad",
            previous_scene_id=scene_2.id
        )
        session.add(scene_3)

        objective_5 = Objective(
            name="break into Hanta's compound, find Bero, if he is there",
            description="break into Hanta's compound, find Bero, if he is there",
            campaign_id=campaign_os_chultanhos.id,
            hidden=False,
            term="short",
            owner="players",
        )
        session.add(objective_5)
        objective_6 = Objective(
            name="avoid capture from either the Minotaur police force or Hanta's Minotaur thugs",
            description="avoid capture from either the Minotaur police force or Hanta's Minotaur thugs",
            campaign_id=campaign_os_chultanhos.id,
            hidden=False,
            term="short",
            owner="players",
        )
        session.add(objective_6)
        objective_7 = Objective(
            name="avenge the destruction of their camp",
            description="avenge the destruction of their camp",
            campaign_id=campaign_os_chultanhos.id,
            hidden=False,
            term="long",
            owner="haemon, oggvay",
        )
        session.add(objective_7)
        objective_8 = Objective(
            name="the coyote told them to learn to fly, but they don't know what it means",
            description="the coyote told them to learn to fly, but they don't know what it means",
            campaign_id=campaign_os_chultanhos.id,
            hidden=False,
            term="long",
            owner="players",
        )
        session.add(objective_8)
        objective_9 = Objective(
            name="remember who they are",
            description="remember who they are",
            campaign_id=campaign_os_chultanhos.id,
            hidden=False,
            term="long",
            owner="spat, dev",
        )
        session.add(objective_9)
        session.commit()
    # ### end Alembic commands ###

def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
