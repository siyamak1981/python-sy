import csv

# CSV = Comma Separated Value


with open('teachers.csv', 'a') as csvfile:
    fieldnames = ['firstname', 'lastname', 'topic']
    teachwriter = csv.DictWriter(csvfile, fieldnames = fieldnames)
    teachwriter.writeheader()
    teachwriter.writerow({
    
        'firstname':'siyamak',
        'lastname':'abasnezhad',
        'topic':'python'

    })


    teachwriter.writerow({
        'firstname':'diyana',
        'lastname':'mohamadi',
        'topic':'django'

    })

