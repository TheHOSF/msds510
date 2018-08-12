# Parse through record and return the markdown format
def create_markdown_record(record, rank):
    md_list = [
        ('# ' + str(rank) + '. ' + record['name_alias'] + '\n\n'),
        ('* Number of Appearances: ' + record['appearances'] + '\n'),
        ('* Year Joined: ' + record['year'] + '\n'),
        ('* Years Since Joining: ' + record['years_since_joining'] + '\n'),
        ('* URL: ' + record['url'] + '\n\n'),
        '## Notes\n\n',
        (record['notes'] + '\n\n')
    ]
    return md_list


# Take a list, filter to top ten records based on appearances
def top_ten_appearance_records(records):
    new_records = sorted(records, key=lambda k: int(k['appearances']), reverse=True)
    top_ten_list = []
    for i in range(10):
        top_ten_list.append(create_markdown_record(new_records[i], i+1))
    return top_ten_list
