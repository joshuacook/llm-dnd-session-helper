from lldm.prompter import Prompter

test_prompt = """Return the following and nothing more:\n\n'Success'"""


def test_prompter_init():
    data = {"test_value": "Success"}
    kind = "test"
    prompter = Prompter(data, kind)

    assert prompter.data == data
    assert prompter.kind == kind
    assert prompter.model == "gpt-3.5-turbo-16k"
    assert prompter.prompt == test_prompt


def test_prompter_gpt_4_init():
    data = {"test_value": "Success"}
    kind = "test"
    prompter = Prompter(data, kind, gpt4=True)

    assert prompter.data == data
    assert prompter.kind == kind
    assert prompter.model == "gpt-4"


def test_prompter_chat():
    data = {"test_value": "Success"}
    kind = "test"
    prompter = Prompter(data, kind)

    result = prompter.chat()
    assert result.replace('"', "") == "Success"
