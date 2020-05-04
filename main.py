import csv

def speak(str):
    from win32com.client import Dispatch 
    speak = Dispatch("sapi.SpVoice")
    speak.Speak(str)

fields = ['First Name', 'Last Name', 'Email ID']

rows = [ ['Rishabh', 'Narayan', 'example@email.com'], 
        ['Ankur', 'Singh', 'abc@example.com'],
        ['Krish', 'Tiwari', 'krish@xyz.com'],
        ['Dhruv', 'Parmar', 'dhruv@sample.com'],
        ['Sourav', 'Kumar', 'sourav@abc.com'],
        ['Shanu', 'Yadav', 'shanu@pqr.com'],
        ['Ankit', 'Mishra', 'ankit@sample.com'],
        ['Ali', 'brothers', 'bandu@abc.com'],
        ['abc', 'xyz', 'pqr@abc.com'],
        ['Aditya', 'Srivastava', 'aditya@example.com']]

with open('contact.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(fields)
    
    for row in rows:
        csv_writer.writerow(row)

with open('contact.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        speak(row)
    csv_file.close()










