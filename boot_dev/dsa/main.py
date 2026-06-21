def count_marketers(job_titles: list[str]) -> int:
    count = 0
    for titles in job_titles:
        if titles.lower() == 'marketer':
            count+=1

    return count    

