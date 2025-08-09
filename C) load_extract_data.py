##loading data into numpy array object
data = np.loadtxt('filename.txt')
#columns to variables
col1,col2,col3,col4 = data.T ##here col1, 2 ,3 4 are the names of the columns and now they are converted into variable names 
print(col1)
#extracting data from the data set
filename = data[:,1:] #this means take all columne but start taking them from the index 1 upto the rest
filename.std(axis=0) ##taking the std columnwise
##which species has the highest polpulation each year??
print(np.argmax(filename, axis=1))
