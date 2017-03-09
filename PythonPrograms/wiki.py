import datetime
import sys

date_list = []
answer_format = '%m/%d'
link_format = '%b_%d'
link = 'https://en.wikipedia.org/wiki/{}'


def create_wiki_links(dates):
  for date in dates:
    try:
      date_format = datetime.datetime.strptime(date, answer_format)
      output = link.format(date_format.strftime(link_format))
      date_list.append(output)
    except ValueError:
      print("That's not a valid date.")
    
def get_dates_from_user():
  print("""What dates would you like? Please use the MM/DD format. Enter 'QUIT' to quit.
        Enter 'DONE' to print links""")
  answer = input(">  ")
  dates = answer.split(', ')
  create_wiki_links(dates)

def print_dates():
  for index, link in enumerate(date_list):
    print('{}: {}'.format(index, link))
    
    
def main():
    get_dates_from_user()
    print_dates()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()

  