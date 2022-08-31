#!/usr/bin/env python3
import os

import aws_cdk as cdk
from bsides import CONSTANTS
from bsides.bsides_stack import BsidesStack


app = cdk.App()
BsidesStack(app, "BsidesStack",
    env=cdk.Environment(account=CONSTANTS.ACCOUNT, region=CONSTANTS.REGION),
    )

app.synth()
