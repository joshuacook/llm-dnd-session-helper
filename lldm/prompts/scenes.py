scenes_prompt = """
Topic: Session Design for D&D Session

RECAP: {{recap}}

A scene can be an interaction, an obstacle, or an encounter.

CONTEXT: {{context}}

MOMENT: {{moment}}

POSSIBLE OUTCOMES: {{possible_outcomes}}

I need three possible scenes for each outcome that will play out in the next five
minutes AFTER this MOMENT. In other words, the players will engage in the MOMENT
and one of the POSSIBLE OUTCOMES will occur. I need three possible NEXT scenes.

A scene can be an interaction, an obstacle, or an encounter.
        
Return the results in the following format:
[
    {   
        "outcome": <OUTCOME>,
        "type": <TYPE>,
        "title": <TITLE>,
        "description": <DESCRIPTION,
    },
    ...
]

Use the short name provided for each outcome.

Please do not reuse any of these scenes: {{scenes}}
{{prompt}}"""
