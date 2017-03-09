import re

string = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''

contacts = re.search(r'(?P<email>[-\w\d.+]+@[-\w\d.]+),\s(?P<phone>\d{3}-\d{3}-\d{4})', string)
twitter = re.search(r'''
                       (@[\w\d]+)$
                    ''', string, re.X)

playersinfo = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''

players = re.search(r'''
                    ^(?P<last_name>[-\w ]+),\s
                    (?P<first_name>[-\w ]+):\s
                    (?P<score>[\d]+)$
                    ''', playersinfo, re.X|re.M)

