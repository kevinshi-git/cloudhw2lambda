
/* UPDATE THE FOLLOWING VARIABLES IN THE CODE

aws-act-no: the account number associated with the Dynamodb table (such as 657065845823
cf-stack-region: the region of the CloudFormation stack (such as us-west-2)
cf-stack-name: name of the CloudFormation responsible for deploying the lambda function
lambda-function-region: the region of the lambda function (such as us-west-2)
s3-bucket-name: name of the S3 bucket where the Lambda function artifacts will be stored

*/


{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:GetObjectVersionTagging",
                "iam:CreateRole",
                "iam:AttachRolePolicy",
                "codedeploy:CreateDeploymentGroup",
                "s3:GetObjectAcl",
                "s3:GetBucketObjectLockConfiguration",
                "iam:DetachRolePolicy",
                "s3:GetObjectVersionAcl",
                "s3:GetBucketPolicyStatus",
                "codedeploy:UpdateApplication",
                "iam:GetRole",
                "s3:GetObjectRetention",
                "s3:GetBucketWebsite",
                "codedeploy:RegisterApplicationRevision",
                "s3:GetJobTagging",
                "iam:DeleteRole",
                "s3:GetObjectLegalHold",
                "s3:GetBucketNotification",
                "s3:GetReplicationConfiguration",
                "s3:ListMultipartUploadParts",
                "s3:GetObject",
                "s3:DescribeJob",
                "codedeploy:DeleteApplication",
                "s3:GetAnalyticsConfiguration",
                "s3:GetObjectVersionForReplication",
                "s3:GetLifecycleConfiguration",
                "codedeploy:CreateApplication",
                "s3:GetBucketTagging",
                "s3:GetInventoryConfiguration",
                "codedeploy:CreateDeployment",
                "codedeploy:GetDeploymentConfig",
                "s3:ListBucketVersions",
                "s3:GetBucketLogging",
                "s3:GetAccelerateConfiguration",
                "codedeploy:UpdateDeploymentGroup",
                "s3:GetBucketPolicy",
                "s3:GetObjectVersionTorrent",
                "s3:GetEncryptionConfiguration",
                "iam:PassRole",
                "s3:GetBucketRequestPayment",
                "s3:GetAccessPointPolicyStatus",
                "s3:GetObjectTagging",
                "s3:GetMetricsConfiguration",
                "s3:GetBucketPublicAccessBlock",
                "s3:ListBucketMultipartUploads",
                "s3:GetBucketVersioning",
                "s3:GetBucketAcl",
                "codedeploy:DeleteDeploymentGroup",
                "s3:GetObjectTorrent",
                "codedeploy:GetDeployment",
                "s3:GetBucketCORS",
                "s3:GetBucketLocation",
                "s3:GetAccessPointPolicy",
                "s3:GetObjectVersion"
            ],
            "Resource": [
                "arn:aws:codedeploy:<us-east-1>:<386726448370>:application:<lambdacfkevinshi>*",
                "arn:aws:codedeploy:<us-east-1>:<386726448370>:deploymentconfig:*",
                "arn:aws:codedeploy:<us-east-1>:<386726448370>:deploymentgroup:<lambdacfkevinshi>*/<lambdacfkevinshi>*",
                "arn:aws:iam::<386726448370>:role/<lambdacfkevinshi>-*",
                "arn:aws:s3:::<codepipelinekevinshi>/*"
            ]
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": [
                "codedeploy:PutLifecycleEventHookExecutionStatus",
                "s3:GetAccessPoint",
                "s3:ListAccessPoints",
                "codedeploy:DeleteGitHubAccountToken",
                "s3:ListJobs",
                "codedeploy:DeleteResourcesByExternalId",
                "codedeploy:StopDeployment",
                "cloudformation:CreateChangeSet",
                "codedeploy:ContinueDeployment",
                "codedeploy:CreateCloudFormationDeployment",
                "s3:GetAccountPublicAccessBlock",
                "cloudformation:CreateStack",
                "cloudformation:DeleteStack",
                "codedeploy:SkipWaitTimeForInstanceTermination"
            ],
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor2",
            "Effect": "Allow",
            "Action": "lambda:*",
            "Resource": "arn:aws:lambda:<us-east-1>:<386726448370>:function:<search-photos>-*"
        }
    ]
}