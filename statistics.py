
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
