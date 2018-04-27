import csv
import json
import pandas as pd

# Read the file Matches Data set.
def read_csv(src) -> list:
    with open(file=src, newline='') as rawFile:
        reader = csv.reader(rawFile)
        # for row in reader:
        #     print(row)
        x = list(reader)
        # for col in reader:
        #     print(col[0], col[1], col[2], col[4], col[5], col[6], col[7], col[10], col[14])
    return x


def map_string_to_int(s: list) -> object:
    """
    :rtype: list
    """
    temp_dict = {}
    counter = 0
    for item in s:
        if counter > 0 and item in temp_dict:
            continue
        else:
            counter = counter + 1
            temp_dict[item] = counter

    k = []
    for item in s:
        k.append(temp_dict[item])

    return k


def write_csv(x: list) -> object:
    # Write the File in a new File
    clean_file = open("./Dataset/matches_cleaned.csv", 'w', newline='')
    with clean_file:
        writer = csv.writer(clean_file)
        writer.writerows(x)
    clean_file.close()


def replace_matched_items(word_list, dictionary):
    for lst in word_list:
        for ind, item in enumerate(lst):
            lst[ind] = dictionary.get(item, item)


if "__main__" == __name__:
    matches_list = read_csv('./Dataset/matches.csv')
    # create a team name list
    team_list = []
    city_list = []
    toss_decision_list = []
    for i in range(len(matches_list)):
        if i != 0:
            team_list.append(matches_list[i][4])
            city_list.append(matches_list[i][2])
            toss_decision_list.append(matches_list[i][7])
    var1 = map_string_to_int(team_list)
    var2 = map_string_to_int(toss_decision_list)
    var3 = map_string_to_int(city_list)

    # create a dict for team names
    team_dict = {}
    for i in range(len(team_list)):
        team_dict[team_list[i]] = var1[i]
    # print(team_dict)
    with open('./jsonDumps/team_dict.json', 'w') as outfile:
        json.dump(team_dict, outfile)

    # create a dict for toss decision

    toss_decision_dict = {}
    for i in range(len(toss_decision_list)):
        toss_decision_dict[toss_decision_list[i]] = var2[i]
    # print(toss_decision_dict)
    with open('./jsonDumps/toss_decision_dict.json', 'w') as outfile:
        json.dump(toss_decision_dict, outfile)

    # create a dict for city

    city_dict = {}
    for i in range(len(city_list)):
        city_dict[city_list[i]] = var3[i]
    # print(city_dict)
    with open('./jsonDumps/city_dict.json', 'w') as outfile:
        json.dump(city_dict, outfile)

    # Replace the matches list with values from these dictionaries
    replace_matched_items(matches_list, team_dict)
    replace_matched_items(matches_list, toss_decision_dict)
    replace_matched_items(matches_list, city_dict)

    write_csv(matches_list)
