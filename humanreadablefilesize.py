from math import floor, log

def humanreadablefilesize(bytes:int) -> str:
    if bytes <= 0:
        return "0.0 B"
    
    units = ["B", "KB","MB", "GB", "TB"]
    exponent = floor(log(bytes, 1024))

    return ' '.join([
        str(round(bytes / pow(1024, exponent),2)),
        units[exponent]
    ])

if __name__ == '__main__':
    print(humanreadablefilesize(100))
    print(humanreadablefilesize(2048))
    print(humanreadablefilesize(20_000_000))
    print(humanreadablefilesize(50_000_000))
