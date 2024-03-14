from pyspark import SparkContext
from pyspark.ml import Pipeline
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import HashingTF, Tokenizer

# Load and parse the data file
sc = SparkContext("local", "Simple App")
data = sc.textFile("data/mllib/sample_libsvm_data.txt").map(lambda x: x.split(" "))

# Transform the data into a numeric representation
tokenizer = Tokenizer(inputCol="value", outputCol="words")
hashingTF = HashingTF(inputCol=tokenizer.getOutputCol(), outputCol="features")
lr = LogisticRegression(maxIter=10, regParam=0.001)
pipeline = Pipeline(stages=[tokenizer, hashingTF, lr])

# Fit the model to the data
model = pipeline.fit(data)