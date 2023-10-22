import pytest
from aws_cdk import App
from aws_cdk.assertions import Template

from vpc_lattice_app.main import MyStack

@pytest.fixture(scope='module')
def template() -> Template:
	app: App = App()
	stack: MyStack = MyStack(app, "my-stack-test")
	template: Template = Template.from_stack(stack)
	yield template

def test_no_buckets_found(template: Template):
	template.resource_count_is("AWS::S3::Bucket", 0)
