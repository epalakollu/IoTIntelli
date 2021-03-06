from socketIO_client import SocketIO, LoggingNamespace
import json
import utils


socketIO = SocketIO(utils.getEnvironmentValueByKey('SOCKET_HOST_NAME'),
                    utils.getEnvironmentValueByKey('SOCKET_PORT'), LoggingNamespace)


def recordStatistics(facetime, total, maleFacesCount, femaleFacesCount):

    statsFile = open("analytics.txt", "a")
    data = {}
    data['date'] = str(facetime.date())+' ' + \
        str(facetime.hour)+':'+str(facetime.minute)
    data['total'] = str(total)
    data['maleFacesCount'] = str(maleFacesCount)
    data['femaleFacesCount'] = str(femaleFacesCount)
    jsonData = json.dumps(data)

    string = str(facetime.date())+' '+str(facetime.hour)+':'+str(facetime.minute) + \
        ','+str(total)+','+str(maleFacesCount)+','+str(femaleFacesCount)

    statsFile.write(string+'\n')
    statsFile.close()

    # with SocketIO('127.0.0.1', 8000, LoggingNamespace) as socketIO:
    socketIO.emit('statsdata', jsonData)
    print(jsonData)


def streamFacesData(maleFaces, femaleFaces):

    if maleFaces > 0 or femaleFaces > 0:
        data = {}
        data['maleFaces'] = str(maleFaces)
        data['femaleFaces'] = str(femaleFaces)
        jsonData = json.dumps(data)

        # with SocketIO('127.0.0.1', 8000, LoggingNamespace) as socketIO:
        socketIO.emit('send faces data', jsonData)
        print(jsonData)
