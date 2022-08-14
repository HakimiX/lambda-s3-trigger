#!/usr/bin/env python3
import os

import aws_cdk as cdk

from lambda_s3_trigger.lambda_s3_trigger_stack import LambdaS3TriggerStack


app = cdk.App()
LambdaS3TriggerStack(app, "LambdaS3TriggerStack")

app.synth()
