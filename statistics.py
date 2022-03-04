
def calculateStats(numbers):
    result = {}
    result["max"] = 0
    result["avg"] = 0
    result["min"] = 0
    if(len(numbers) > 0):
        sum = 0
        for i in range(len(numbers)):
            if(i == 0):
                result["max"] = numbers[i]
                result["min"] = numbers[i]
            if(result["max"] < numbers[i]):
                result["max"] = numbers[i]
            if(result["min"] > numbers[i]):
                result["min"] = numbers[i]
            sum += numbers[i]
        result["avg"] = sum/len(numbers)
        return result
    else:
        result["avg"] = float("Nan")
    return result

class EmailAlert:
    def __init__(self):
        self.emailSent = False


class LEDAlert:
    def __init__(self):
        self.ledGlows=False


class StatsAlerter:
    def __init__(self, maxThreshold, inputs):
        self.MaxThreshold = maxThreshold
        self.alerters=inputs

    def checkAndAlert(self, numbers):
        result = calculateStats(numbers)
        if(result["max"] > self.MaxThreshold):
            self.alerters[0].emailSent=True
            self.alerters[1].ledGlows=True
