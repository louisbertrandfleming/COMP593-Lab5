'''dadjokes.py - Request a dad joke and paste to pastebin.
COMP 593 Scripting Applications Winter 2025 Lab 5
Louis Bertrand <louis.bertrand@flemingcollege.ca>

Usage:
python dadjokes.py <subject>
where subject is a keyword to search in the dad jokes database.

'''


from sys import argv
import dadjokes_api
import pastebin_api

def get_subject():
    '''Get the joke subject from the command line, e.g. kids, cars, etc.
    Return the word as a string, trimmed of leading and trailing blanks,
    and mapped to lowercase.
    '''
    if len(argv) > 1:
        return str(argv[1]).strip().lower()
    else:
        print("Expecting joke subject on command line, exiting...")
        exit()

def main():
    subject = get_subject()
    joke_data = dadjokes_api.fetch_joke(subject)
    # Reformat data from dadjokes site
    paste_url = pastebin_api.pastebin_post(joke_data)
    print(paste_url)

if __name__ == "__main__":
    main()
