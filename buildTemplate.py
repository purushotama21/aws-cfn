import os

# Variables
LINE_BREAKER = "\n\n"
currentDirectory = os.getcwd()
masterTemplateFile = currentDirectory + '/template.yaml'

# Open the master template file
print('Creating master template: ' + masterTemplateFile)
masterTemplate = open(masterTemplateFile, 'w')

########################################################################################################
# Concatenate the CloudFormation Templates
########################################################################################################
try:
    subdir = currentDirectory + '/cloudformation1/'
    cloudformationFiles = sorted(os.listdir(subdir))

    # Write CloudFormation header to master template first.
    headerFile = open(subdir + 'header.yaml', 'r')
    headerFileContents = headerFile.read()
    masterTemplate.write(headerFileContents)
    headerFile.close()

    for file in cloudformationFiles:
        if file != 'header.yaml':   # Make sure we don't write header.yaml again.
            inFile = open(subdir + file, 'r')
            inFileContents = inFile.read()
            masterTemplate.write(LINE_BREAKER + inFileContents)
            inFile.close()

except:
    print("CloudFormation Template concatenation failed")

# Close master template file
masterTemplate.close()
