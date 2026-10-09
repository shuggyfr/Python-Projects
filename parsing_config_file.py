def parse_config(filename):

    parsed = {}
    with open(filename) as f:


        for line in f:
            line = line.strip()

            if line == "":
                continue

            if line.startswith('#'):
                continue

            parts = line.split(":",1)
            key = parts[0].strip()
            value = parts[1].strip()
            parsed[key]=value

        return parsed
print(parse_config('config.txt'))



                        