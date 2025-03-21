from pyspark.sql import types as T

T.StructType(
    [
        T.StructField("atoll_site_id", T.StringType(), False),
        T.StructField("modernization", T.DecimalType(), True),
        T.StructField("l2100_ca", T.DecimalType(), True),
        T.StructField("l2100_10mhz", T.TimestampType(), True),
        T.StructField("u900_dc", T.StringType(), True),
        T.StructField("l900", T.DecimalType(), True),
        T.StructField("six_sect", T.DecimalType(), True),
        T.StructField("sectorization", T.TimestampType(), True),
        T.StructField("nb_iot", T.StringType(), True),
        T.StructField("boost_3g", T.DecimalType(), True),
        T.StructField("boost_4g", T.DecimalType(), True),
        T.StructField("rain_name", T.TimestampType(), True),
        T.StructField("rain_ca", T.StringType(), True),
        T.StructField("live_site", T.DecimalType(), True),
    ]
)