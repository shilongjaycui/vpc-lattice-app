from projen.awscdk import AwsCdkPythonApp

project = AwsCdkPythonApp(
    author_email="shilongjaycui@gmail.com",
    author_name="Jay Cui",
    cdk_version="2.1.0",
    module_name="vpc_lattice_app",
    name="vpc-lattice-app",
    version="0.1.0",
)

project.synth()