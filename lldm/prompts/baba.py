baba_prompt = """
Topic: Add a little Baba Magic to D&D Scenes

CONTEXT: {{context}}

MOMENT: {{moment}}

POSSIBLE OUTCOMES: {{possible_outcomes}}

This adventure takes place in a land straddling two realities: the Fey Wild and the
Fey Wastes. Both of these are magical lands where anything can and often does happen.
But also the reality is unstable. Physics may momentarily start misbehaving. At the
center of this is Baba Magic, the distilled magic collected when the Seelie Court was
destroyed. This magic is now being weilded by a Rakshasa, but he's not quite in control
of it. IMPORTANT: THE PLAYERS CAN BE TOLD NONE OF THIS. THIS IS MERELY IMPORTANT
BACKGROUND TO THE NEXT REQUEST.

Here is a list of scenes: 

{{scenes}}

The magic effects should be chosen from a random magic effects table. 

Can you imbue each of the descriptions of these scenes with baba magic. Return them in
EXACTLY the same format. Please do not literally say "Baba Magic".

"""
