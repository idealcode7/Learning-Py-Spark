# Databricks notebook source
# MAGIC %md
# MAGIC # Creating Session 
# MAGIC

# COMMAND ----------

from pyspark.sql import SparkSession
spark = SparkSession.builder \
        .appName("My spark app") \
          .getOrCreate()


# COMMAND ----------


