from poetry_cdk_plugin.command import SynthCommand
from tests.mesgs import WRONG_CMD, WRONG_DESC, WRONG_CLI_ARG


def test_synth_cmd_definition():
    assert SynthCommand.name == "cdk synth", WRONG_CMD
    expected_desc = "Synth a CDK application"
    assert SynthCommand.description == expected_desc, WRONG_DESC


def test_synth_cmd_cdk_cli_args():
    synth_command = SynthCommand()
    assert synth_command.cdk_cli_args == ["synth"], WRONG_CLI_ARG
