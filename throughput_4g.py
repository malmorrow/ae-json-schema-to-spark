from pyspark.sql import types as T

T.StructType(
    [
        T.StructField("atoll_site_id", T.StringType(), False),
        T.StructField("avg_dl_throughput_mbps", T.DecimalType(), True),
        T.StructField("avg_ul_throughput_mbps", T.DecimalType(), True),
        T.StructField("date_time", T.TimestampType(), True),
    ]
)