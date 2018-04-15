from subprocess import run, PIPE

def isNumber(s):
    return any(char.isdigit() for char in s)

def command(cmdString):
    return cmdString.split()

def deleteFileContent(filename):
    file = open(filename, mode='w')
    file.write('')
    file.close()

def writeFile(filename, cmdOutput):
    file = open(filename, mode='a')
    file.write(
        '<?xml version="1.0" encoding="utf-8"?>\n'+
        '<packages>\n'
    )

    for text in cmdOutput:
        if (text.__contains__('package')):
            break
        if ( isNumber(text) == False ):
            file.write('<package id="'+text+'" />\n')

    file.write(
        '</packages>'
    )
    
    file.close()

    print(filename + ' file created')

filename = 'packages.config'

cmdOutput = run(command('choco list -lo'), stdout=PIPE).stdout.decode('utf-8')

deleteFileContent(filename)

writeFile(filename, cmdOutput.split())