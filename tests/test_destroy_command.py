from poetry_cdk_plugin.command import DestroyCommand
from tests.mesgs import WRONG_CMD, WRONG_DESC, WRONG_CLI_ARG


def test_destroy_cmd_definition():
    assert DestroyCommand.name == "cdk destroy", WRONG_CMD
    exp_desc = "Destroy a CDK application"
    assert DestroyCommand.description == exp_desc, WRONG_DESC


def test_destroy_cmd_cdk_cli_args():
    destroy_command = DestroyCommand()
    exp_args = [
        "destroy",
        '"*"',
        "--force",
    ]
    assert destroy_command.cdk_cli_args == exp_args, WRONG_CLI_ARG
