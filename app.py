import os
from aws_cdk import App, Environment
# from vpc_lattice_app.stack import MyStack


app = App()

# for development, use account/region from cdk cli
dev_env = Environment(
  account=os.getenv('CDK_DEFAULT_ACCOUNT'),
  region=os.getenv('CDK_DEFAULT_REGION')
)
# MyStack(app, "vpc-lattice-app-dev", env=dev_env)
# MyStack(app, "vpc-lattice-app-prod", env=prod_env)

app.synth()