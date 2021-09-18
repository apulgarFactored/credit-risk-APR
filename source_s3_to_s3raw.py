import sys
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from awsglue.dynamicframe import DynamicFrame

## Getting context to use aws/spark tools and access to them

glue_context = GlueContext(SparkContext.getOrCreate())
glue_job = Job(glue_context)
args = getResolvedOptions(sys.argv, ["JOB_NAME"])

glue_job.init(args["JOB_NAME"], args)
spark_session = glue_context.sparkSession

#ETL, extract data from s3 bucket them put it into another bucket called raw_zone s3://onboarding-projects/credit_default/

#Extracting data from s3
bureau_balance_df = spark_session.read.format("csv").options (
    header = "true",
    inferSchema = "true",
).load("s3://onboarding-projects/credit_default/bureau_balance.csv")

bureau_df = spark_session.read.format("csv").options (
    header = "true",
    inferSchema = "true",
).load("s3://onboarding-projects/credit_default/bureau.csv")

credit_card_balance_df = spark_session.read.format("csv").options (
    header = "true",
    inferSchema = "true",
).load("s3://onboarding-projects/credit_default/credit_card_balance.csv")

installments_payments_df = spark_session.read.format("csv").options (
    header = "true",
    inferSchema = "true",
).load("s3://onboarding-projects/credit_default/installments_payments.csv")

previous_application_df = spark_session.read.format("csv").options (
    header = "true",
    inferSchema = "true",
).load("s3://onboarding-projects/credit_default/previous_application.csv")

pos_cash_balance_df = spark_session.read.format("csv").options (
    header = "true",
    inferSchema = "true",
).load("s3://onboarding-projects/credit_default/POS_CASH_balance.csv")


print(bureau_balance.limit(10))

###Converting Spark data frames on dynamic frames to write into raw_zone
bureau_balance_dynamic = DynamicFrame.fromDF(
    bureau_balance_df,
    glue_context,
    "bureau_balance"
)

bureau_dynamic = DynamicFrame.fromDF(
    bureau_df,
    glue_context,
    "bureau"
)

credit_card_balance_dynamic = DynamicFrame.fromDF(
    credit_card_balance_df,
    glue_context,
    "credit_card_balance"
)

installments_payments_dynamic = DynamicFrame.fromDF(
    installments_payments_df,
    glue_context,
    "installments_payments"
)

pos_cash_balance_dynamic = DynamicFrame.fromDF(
    pos_cash_balance_df,
    glue_context,
    "POS_CASH_balance"
)

previous_application_dynamic = DynamicFrame.fromDF(
    previous_application_df,
    glue_context,
    "previous_application"
)


##Writing results on s3 bucket raw_zone
glue_context.write_dynamic_frame.from_options(
    frame = bureau_balance_dynamic,
    connection_options = {"path": "s3://onboarding-projects/andres_pulgarin/raw_zone"},
    connection_type = "s3",
    format = "csv",
    transformation_ctx = "from s3 source to s3 raw_zone"
)

glue_context.write_dynamic_frame.from_options(
    frame = bureau_dynamic,
    connection_options = {"path": "s3://onboarding-projects/andres_pulgarin/raw_zone"},
    connection_type = "s3",
    format = "csv",
    transformation_ctx = "from s3 source to s3 raw_zone"
)
 
glue_context.write_dynamic_frame.from_options(
    frame = credit_card_balance_df,
    connection_options = {"path": "s3://onboarding-projects/andres_pulgarin/raw_zone"},
    connection_type = "s3",
    format = "csv",
    transformation_ctx = "from s3 source to s3 raw_zone"
)

glue_context.write_dynamic_frame.from_options(
    frame = pos_cash_balance_dynamic,
    connection_options = {"path": "s3://onboarding-projects/andres_pulgarin/raw_zone"},
    connection_type = "s3",
    format = "csv",
    transformation_ctx = "from s3 source to s3 raw_zone"
)

glue_context.write_dynamic_frame.from_options(
    frame = installments_payments_dynamic,
    connection_options = {"path": "s3://onboarding-projects/andres_pulgarin/raw_zone"},
    connection_type = "s3",
    format = "csv",
    transformation_ctx = "from s3 source to s3 raw_zone"
)

glue_context.write_dynamic_frame.from_options(
    frame = previous_application_dynamic,
    connection_options = {"path": "s3://onboarding-projects/andres_pulgarin/raw_zone"},
    connection_type = "s3",
    format = "csv",
    transformation_ctx = "from s3 source to s3 raw_zone"
)

glue_job.commit()