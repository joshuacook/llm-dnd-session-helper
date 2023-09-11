import html
import openai
import dataclasses
import jinja2


@dataclasses.dataclass
class Prompter:
    data: dict
    kind: str = ""
    kinds: list[str] = dataclasses.field(default_factory=list)
    gpt4: bool = False

    def __post_init__(self):
        self.prompts = []
        if self.kind != "":
            self.kinds = [self.kind] + self.kinds
        for kind in self.kinds:
            self.prompts.append(self.prepare_prompt(kind))
        self.prompt = "\n".join(self.prompts)

        if self.gpt4:
            self.model = "gpt-4"
        else:
            self.model = "gpt-3.5-turbo-16k"

    def chat(self) -> str:
        messages = [{"role": "user", "content": self.prompt}]
        chat = openai.ChatCompletion.create(model=self.model, messages=messages)
        return chat["choices"][0]["message"]["content"]

    def prepare_prompt(self, kind):
        env = jinja2.Environment(loader=jinja2.FileSystemLoader("./lldm/prompts/"))
        template = env.get_template(f"{kind}.jinja")
        return html.unescape(template.render(self.data))
