import numpy, matplotlib
import matplotlib.pyplot as plt

polynomialOrder = 1 # example quadratic
import numpy as np
import pylab
import matplotlib.pyplot as plt
from scipy.stats import linregress


x=[26.835, 30.003, 31.962, 39.875]
y=[1517, 1533, 1549, 1571]

yData =np.log(x)
xData =np.log(y)

# curve fit the test data
fittedParameters = numpy.polyfit(xData, yData, polynomialOrder)
print('Fitted Parameters:', fittedParameters)

modelPredictions = numpy.polyval(fittedParameters, xData)
absError = modelPredictions - yData

SE = numpy.square(absError) # squared errors
MSE = numpy.mean(SE) # mean squared errors
RMSE = numpy.sqrt(MSE) # Root Mean Squared Error, RMSE
Rsquared = 1.0 - (numpy.var(absError) / numpy.var(yData))
print('RMSE:', RMSE)
print('R-squared:', Rsquared)

print()


##########################################################
# graphics output section
def ModelAndScatterPlot(graphWidth, graphHeight):
    f = plt.figure(figsize=(graphWidth/100.0, graphHeight/100.0), dpi=100)
    axes = f.add_subplot(111)

    # first the raw data as a scatter plot
    axes.plot(xData, yData,  'D')

    # create data for the fitted equation plot
    xModel = numpy.linspace(min(xData), max(xData))
    yModel = numpy.polyval(fittedParameters, xModel)

    # now the model as a line plot
    axes.plot(xModel, yModel)
    plt.title('Curve Fit of log(q) vs log(V) ')
    axes.set_xlabel('log(V)') # X axis data label
    axes.set_ylabel('log(q)') # Y axis data label
    plt.legend(['Data points','log(q) = 10.99393403 * log(V) -77.24698074'])
    plt.show()
    axes.grid()
    plt.close('all') # clean up after using pyplot

graphWidth = 800
graphHeight = 600
ModelAndScatterPlot(graphWidth, graphHeight)
