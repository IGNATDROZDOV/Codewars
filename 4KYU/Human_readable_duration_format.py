def format_duration(seconds):
    format_time = {"years":seconds//31536000,
    "days":seconds%31536000//86400,
    "hours":seconds%31536000%86400//3600,
    "minutes":seconds%31536000%86400%3600//60,
    "seconds":seconds%31536000%86400%3600%60}
    format_time = {key:val for key,val in format_time.items() if val!=0}
    d = {
        0: "now",
        1: "{}",
        2: "{} and {}",
        3: "{}, {} and {}",
        4: "{}, {}, {} and {}",
        5: "{}, {}, {}, {} and {}"
        }
    format_time = ['{} {}'.format(val, key) if val > 1 else '{} {}'.format(val, key[:-1]) for key,val in format_time.items()]
    length = len(format_time)
    return d[length].format(*format_time)