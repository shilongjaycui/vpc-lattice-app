import pytest
from aws_cdk import App, Stack
from aws_cdk import aws_sns as sns
from aws_cdk.assertions import Template

from vpc_lattice_app.stack import StateMachineStack

@pytest.fixture(scope='module')
def template() -> Template:
	app: App = App()

	# Since the StateMachineStack consumes resources from a separate stack
    # (cross-stack references), we create a stack for our SNS topics to live
    # in here. These topics can then be passed to the StateMachineStack later,
    # creating a cross-stack reference.
	topics_stack: Stack = Stack(app, "TopicsStack")

	# Create the topic the stack we're testing will reference.
	topics = [sns.Topic(topics_stack, "Topic1")]

	# Create the StateMachineStack.
	state_machine_stack: StateMachineStack = StateMachineStack(
		app,
		"StateMachineStack",
		topics=topics,  # Cross-stack reference
	)

	# Prepare the stack for assertions.
	template: Template = Template.from_stack(state_machine_stack)
	yield template

def test_no_buckets_found(template: Template):
	template.resource_count_is("AWS::S3::Bucket", 0)

def test_synthesizes_properly(template: Template):
	# Assert that we have created the function with the correct properties
	template.has_resource_properties(
        "AWS::Lambda::Function",
        {
            "Handler": "handler",
            "Runtime": "python3.11",
        },
    )

    # Assert that we have created a subscription
	template.resource_count_is("AWS::SNS::Subscription", 1)

