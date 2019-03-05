import csv

data = list(csv.DictReader(open('Resources/election_data.csv', 'r')))
total_votes = len(data)
candidates = []  # Contains names of all candidates
vote_list = []  # Contains each candidates' voters in a list, the len of this is the same as len of candidates
current_index = 0
winner_list = []
winner = ''

f = open('Result.txt', 'w')

for vote in data:
    if vote['Candidate'] not in candidates:
        candidates.append(vote['Candidate'])

for candidate in candidates:
    vote_list.append(list(filter(lambda person: person['Candidate'] == candidates[current_index], data)))
    current_index += 1

print('Election Results\n------------------------------\nTotal Votes: {}\n------------------------------\n'.format(
    total_votes))

f.write('Election Results\n------------------------------\nTotal Votes: {}\n------------------------------\n'.format(
    total_votes))

for vote_item in vote_list:
    vote_item.append(
        {vote_item[0]['Candidate']: len(vote_item)})
    # print(vote_item[-1])
    print(vote_item[0]['Candidate'] + ': ' + str(
        round(vote_item[-1][vote_item[0]['Candidate']] / total_votes * 100, 3))
          + '% (' + str(
        vote_item[-1][vote_item[0]['Candidate']]) + ')\n')
    f.write(vote_item[0]['Candidate'] + ': ' + str(
        round(vote_item[-1][vote_item[0]['Candidate']] / total_votes * 100, 3))
            + '% (' + str(
        vote_item[-1][vote_item[0]['Candidate']]) + ')\n')
    winner_list.append(vote_item[-1][vote_item[0]['Candidate']])

maximum_votes = max(winner_list)

for vote_item in vote_list:
    if vote_item[-1][vote_item[0]['Candidate']] == maximum_votes:
        winner = vote_item[0]['Candidate']

print('\n------------------------------\nWinner: {}\n------------------------------\n'.format(winner))

f.write('\n------------------------------\nWinner: {}\n------------------------------\n'.format(winner))
