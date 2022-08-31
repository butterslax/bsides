import aws_cdk as core
import aws_cdk.assertions as assertions

from bsides.bsides_stack import BsidesStack

# example tests. To run these tests, uncomment this file along with the example
# resource in bsides/bsides_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = BsidesStack(app, "bsides")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
