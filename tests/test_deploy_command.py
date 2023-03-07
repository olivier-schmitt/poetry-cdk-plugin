from poetry_cdk_plugin.command import DeployCommand
from tests.mesgs import WRONG_CMD, WRONG_DESC, WRONG_CLI_ARG


def test_deploy_cmd_definition():
    assert DeployCommand.name == "cdk deploy", WRONG_CMD
    exp_desc = "Deploy a CDK application"
    assert DeployCommand.description == exp_desc, WRONG_DESC


def test_deploy_cmd_cdk_cli_args():
    deploy_command = DeployCommand()
    exp_args = [
        "deploy",
        '"*"',
        "--require-approval",
        "never",
    ]
    assert deploy_command.cdk_cli_args == exp_args, WRONG_CLI_ARG
