import html
import openai
import dataclasses
import jinja2

import lldm.prompts as prompts


@dataclasses.dataclass
class Prompter:
    data: dict
    kind: str
    gpt4: bool = False

    def __post_init__(self):
        self.prepare()
        if self.gpt4:
            self.model = "gpt-4-32k"
        else:
            self.model = "gpt-3.5-turbo-16k"

    def chat(self) -> str:
        messages = [{"role": "user", "content": self.prompt}]
        chat = openai.ChatCompletion.create(model=self.model, messages=messages)
        return chat["choices"][0]["message"]["content"]
    
    def prepare(self):
        self.template = getattr(prompts, f"{self.kind}_prompt") 
        env = jinja2.Environment(loader=jinja2.BaseLoader())
        template = env.from_string(self.template)
        self.prompt = html.unescape(template.render(self.data))
