# Databricks notebook source
# MAGIC %md
# MAGIC ## Magic command FS

# COMMAND ----------

display(dbutils.fs.ls('/'))

# COMMAND ----------

display(dbutils.fs.ls('/databricks-datasets'))

# COMMAND ----------

f=open('/dbfs/databricks-datasets/README.md','r')
print = f.read()

# COMMAND ----------

# MAGIC %fs ls /databricks-datasets//Rdatasets

# COMMAND ----------

f=open('/dbfs/databricks-datasets/Rdatasets/README.md','r')
print = f.read()

# COMMAND ----------

f=open('/dbfs/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv','r')
print = f.read()

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC  DROP TABLE IF EXISTS diamonds;
# MAGIC  CREATE TABLE diamonds USING CSV OPTIONS (path = "/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv", header "true");
