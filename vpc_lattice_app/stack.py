import aws_cdk as cdk
import aws_cdk.aws_lambda as lambda_
from aws_cdk.aws_ec2 import Vpc

from constructs import Construct


class StateMachineStack(cdk.Stack):
	def __init__(
			self,
			scope: Construct,
			construct_id: str,
			**kwargs,
	) -> None:
		super().__init__(scope, construct_id, **kwargs)

        # This Lambda function says hello.
		lambda_function: lambda_.Function = lambda_.Function(
            self,
            "LambdaFunction",
            runtime=lambda_.Runtime.PYTHON_3_11,
            handler="handler",
            code=lambda_.Code.from_asset("../lambda"),
        )

		"""
		TODO: configure the following for the VPC
			- IP address range
			- subnets
				- must be connected to a network access control list, which allows
					inbound and outbound traffic
				- route tables
					- must have a route to the internet gateway below
			- internet gateways
			- security groups
		
		"""
		billing_vpc: Vpc = Vpc()
		parking_vpc: Vpc = Vpc()