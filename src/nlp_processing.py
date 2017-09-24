import json
import nifty_sql

def get_dict():
    humiditiy = ['humid', 'muggy', 'mugginess', 'humidness', 'stuffy', 'stuffiness', 'dampness', 'damp', 'dankness', 'dank', 'moisture', 'moist', 'moistness', 'wetness', 'wet', 'humidity']
    temperature = ['temperature', 'hot', 'cold', 'weather']
    sound = ['loud', 'noisy', 'forte', 'fortissimo', 'quiet', 'soft', 'rowdy', 'decibel', 'decibels', 'shout', 'shouting', 'screaming', 'loudness', 'noisiness']
    number = "???"
    time_period = ['now', ' minute', 'hour', 'day', 'week', 'month']

    return {
        'humidity' : humiditiy,
        'temperature' : temperature,
        'sound' : sound,
        'number' : number,
        'time_period' : time_period,
    }


def get_number(input_text_list):
    """

    :param input_text_list:
    :return: Possible values:
            Any integer with the default being 1.
    """
    numbers = {}

    for word in input_text_list:
        if word.isdigit():
            num = int(word)
            numbers[num] = numbers.setdefault(num, 0) + 1

    sums = numbers.keys()

    maximum = max(sums)


    # The default value is that the units is just one ("...over the past week" should evaluate to one unit)
    if maximum == 0:
        return 1
    elif sums.count(maximum) > 1:
        return 1
    else:
        for k, v in numbers.iteritems():
            if maximum == v:
                return k

def get_category(input_text_list):
    """
    :param input_text_list:
    :return:  Possible values:
                "no max", "tie", "humidity", "temperature", "sound"
    """
    d = get_dict()

    humidity_sum = 0
    temperature_sum = 0
    sound_sum = 0
    for h in d['humidity']:
        humidity_sum += input_text_list.count(h)
    for t in d['temperature']:
        temperature_sum += input_text_list.count(t)
    for s in d['sound']:
        sound_sum += input_text_list.count(s)

    maximum = max(humidity_sum, temperature_sum, sound_sum)

    if maximum == 0:
        return "no max"
    elif [humidity_sum, temperature_sum, sound_sum].count(maximum) > 1:
        return "tie"
    else:
        if humidity_sum == maximum:
            return "humidity"
        elif temperature_sum == maximum:
            return "temperature"
        else:
            return "sound"

def get_time_period(input_text_list):
    """

    :param input_text_list:
    :return: Possible values:
                'no max', 'tie', 'now', ' minute', 'hour', 'day', 'week', 'month'
    """

    timeframes = get_dict()['time_period']

    sums = [0]*len(timeframes)

    # Sums up number of occurences of each time frame word. Also accounts for plurals --> week and weeks
    for i, t in enumerate(timeframes):
        for word in input_text_list:
            if t in word:
                sums[i] += 1

    maximum = max(sums)

    if maximum == 0:
        return "no max"
    elif sums.count(maximum) > 1:
        return "tie"
    else:
        return timeframes[sums.index(maximum)]



def parse_speech_text_json(json_file):
    obj = json.load(f)
    text_list = []
    for i in obj["NBest"]:
        disp = i['Display']
        disp = disp.strip(".?,;:\\/'\"").lower()
        text_list.extend(disp.split(" "))
    return text_list

get_dict()


with open("./voice_to_text_json.json", "r") as f:
    text_list = parse_speech_text_json(f)

category = get_category(text_list)
time_period = get_time_period(text_list)
number = get_number(text_list)

print category, time_period, number

print nifty_sql.sql_query()['Temperature'].describe()['max']