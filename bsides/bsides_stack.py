import aws_cdk as cdk
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_iam as iam
from constructs import Construct

# import bsides.CONSTANTS as CONSTANTS


class BsidesStack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        s3Bucket = s3.Bucket(
            self,
            "Bsides Test Bucket",
            bucket_name="typarro-bsides-test-bucket",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
        )
        # s3Bucket.add_to_resource_policy(
        #    iam.PolicyStatement(
        #        actions=["s3:*"],
        #        resources=[s3Bucket.arn_for_objects("*")],
        #        principals=[iam.AccountPrincipal(account_id=CONSTANTS.ACCOUNT)],
        #    )
        # )
