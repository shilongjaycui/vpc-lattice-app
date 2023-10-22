from typing import List

import aws_cdk as cdk
import aws_cdk.aws_lambda as lambda_
import aws_cdk.aws_sns as sns
import aws_cdk.aws_sns_subscriptions as sns_subscriptions
import aws_cdk.aws_stepfunctions as sfn

from constructs import Construct


class StateMachineStack(cdk.Stack):
	def __init__(
			self,
			scope: Construct,
			construct_id: str,
			*,
			topics: List[sns.Topic],
			**kwargs
	) -> None:
		super().__init__(scope, construct_id, **kwargs)
		# The code that defines your stack goes here

		# In the future this state machine will do some work...
		state_machine: sfn.StateMachine = sfn.StateMachine(
            self, "StateMachine", definition=sfn.Pass(self, "StartState")
        )

        # This Lambda function starts the state machine.
		lambda_function: lambda_.Function = lambda_.Function(
            self,
            "LambdaFunction",
            runtime=lambda_.Runtime.PYTHON_3_11,
            handler="handler",
            code=lambda_.Code.from_asset("../lambda"),
            environment={
                "STATE_MACHINE_ARN": state_machine.state_machine_arn,
            },
        )
		state_machine.grant_start_execution(lambda_function)

		subscription: sns_subscriptions.LambdaSubscription = sns_subscriptions.LambdaSubscription(lambda_function)
		for topic in topics:
			topic.add_subscription(subscription)