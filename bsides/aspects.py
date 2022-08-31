from aws_cdk import (
    IAspect,
    Stack,
    aws_s3 as s3,
    Annotations,
    Tokenization,
)
from constructs import IConstruct
import jsii


@jsii.implements(IAspect)
class s3_version_aspect:
    def visit(self, node):
        if isinstance(node, s3.CfnBucket):
            if (
                not node.versioning_configuration
                or not Tokenization.is_resolvable(node.versioning_configuration)
                and node.versioning_configuration.status != "Enabled"
            ):
                Annotations.of(node).add_error("S3 bucket versioning is not enabled")


@jsii.implements(IAspect)
class s3_encryption_aspect:
    def visit(self, node):
        if isinstance(node, s3.CfnBucket):

            if not Stack.of(node).resolve(node.bucket_encryption):
                return Annotations.of(node).add_error(
                    "S3 bucket must have encryption enabled (encryption=s3.BucketEncryption.KMS_MANAGED)"
                )
            else:
                encryption = Stack.of(node).resolve(
                    node.bucket_encryption.server_side_encryption_configuration
                )
                sse = Stack.of(node).resolve(
                    encryption[0]["serverSideEncryptionByDefault"]["sseAlgorithm"]
                )
                if sse != "aws:kms":
                    return Annotations.of(node).add_error(
                        "S3 encrption set to %s but it should be set to KMS_MANAGED"
                        % sse
                    )
