def file_read_from_head(name, nlines):
        from itertools import islice
        with open(name) as f:
                for line in islice(f, nlines):
                        print(line)
file_read_from_head('text.txt',2)