from aws_cdk import (
    aws_lambda as _lambda,
    aws_s3 as _s3,
    aws_s3_notifications as s3_notification,
    Stack
)
from constructs import Construct

class LambdaS3TriggerStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # Lambda function
        lambda_function = _lambda.Function(
            self, 'lambda_function',
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="lambda.handler",
            code=_lambda.Code.from_asset('./lambda')
        )

        # S3 bucket
        s3_bucket = _s3.Bucket(self, 's3_bucket')

        # S3 notification for lambda function
        notification = s3_notification.LambdaDestination(lambda_function)

        # assign notification for the s3 event type (ex: OBJECT_CREATED)
        s3_bucket.add_event_notification(_s3.EventType.OBJECT_CREATED, notification)