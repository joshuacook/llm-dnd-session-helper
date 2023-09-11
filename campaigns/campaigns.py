from lldm.models import Campaign

from sqlmodel import SQLModel, Session, create_engine, select

engine = create_engine("sqlite:///lldm.db")
SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    statement = select(Campaign).where(
        Campaign.name == "The Fey Wastes" and Campaign.party == "Os Chultanhos"
    )

    if session.exec(statement).first() is None:
        campaign = Campaign(
            name="The Fey Wastes",
            description="In the desolate Fey Wastes, desert tribe members embark on a quest to rescue a kidnapped brother after the destruction of their camp and annihilation of their people by a gang of Minotaurs. Joined by two amnesiac Eladrin who recently wandered out of the desert, the party ventures deeper into the mysteries of this barren land.",  # noqa
            party="Os Chultanhos",
        )
        session.add(campaign)
        session.commit()
        session.refresh(campaign)
        print("Created campaign: ", campaign)

    statement = select(Campaign).where(
        Campaign.name == "The Fey Wastes" and Campaign.party == "Los Perdidos"
    )

    if session.exec(statement).first() is None:
        campaign = Campaign(
            name="The Fey Wastes",
            description="In the desolate Fey Wastes, desert tribe members embark on a quest to rescue a kidnapped brother after the destruction of their camp and annihilation of their people by a gang of Minotaurs. Joined by two amnesiac Eladrin who recently wandered out of the desert, the party ventures deeper into the mysteries of this barren land.",  # noqa
            party="Los Perdidos",
        )
        session.add(campaign)
        session.commit()
        session.refresh(campaign)
        print("Created campaign: ", campaign)
