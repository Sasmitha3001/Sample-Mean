import statistics
import random 
import csv
import plotly.figure_factory as ff
import pandas as pd


data=pd.read_csv('newdata.csv')
data1=data["average"].tolist()

mean=statistics.mean(data1)
std_dev=statistics.stdev(data1)
print('mean={},standard deviation{}'.format(mean,std_dev))

# fig=ff.create_distplot([data1],["Average"],show_hist=False)
# fig.show()

def randomSetOfMean():
    dataset=[]

    for i in range(0,100):
        index1=random.randint(0,len(data1)-1)
        value=data1[index1]
        dataset.append(value)

    dataset_mean=statistics.mean(dataset)
    #dataset_stdDev=statistics.stdev(dataset)
    return dataset_mean

#print('mean={},standard deviation{}'.format(dataset_mean,dataset_stdDev))


# figure=ff.create_distplot([dataset],["Random Average Data"],show_hist=False)
# figure.show()

def setup():
    sampleMeanDistribution=[]
    for i in range(0,1000):
        x=randomSetOfMean()
        sampleMeanDistribution.append(x)
    sampleMean=statistics.mean(sampleMeanDistribution)
    print("Sample Mean =",sampleMean)

    sample_std=statistics.stdev(sampleMeanDistribution)
    print("Std dev =",sample_std)

    figure=ff.create_distplot([sampleMeanDistribution],["Sample Mean"],show_hist=False)
    figure.show()

setup()




