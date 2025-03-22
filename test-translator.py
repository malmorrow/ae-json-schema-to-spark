import unittest
from pyspark.sql import types as T

class RanSitelistForTx(unittest.TestCase):
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

class Test(unittest.TestCase): 
    # test function to test whether obj is instance of class 
    def test_negative(self): 
        objectName = RanSitelistForTx() 
        message = "given object is not instance of RanSitelistForTx."
        self.assertIsInstance(objectName, RanSitelistForTx, message) 

if __name__ == '__main__': 
    unittest.main() 