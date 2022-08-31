#!/usr/bin/env python3
import os

import aws_cdk as cdk
from aws_cdk import Aspects

# from bsides import CONSTANTS
from bsides.bsides_stack import BsidesStack

from bsides.aspects import s3_version_aspect, s3_encryption_aspect

app = cdk.App()
test_stack = BsidesStack(
    app,
    "BsidesStack",
    # env=cdk.Environment(account=CONSTANTS.ACCOUNT, region=CONSTANTS.REGION),
)

Aspects.of(test_stack).add(s3_encryption_aspect())
app.synth()
