conversation1 = {
    'number1': '+91 99999 11111',
    'number2': '+91 99999 22222',
    'messages': [
        {
            'text': 'Hello',
            'sender': '+91 99999 11111',
            'timeStamp': '16:10',
            'status': 1
        },
        {
            'text': 'Hi, How are you ?',
            'sender': '+91 99999 22222',
            'timeStamp': '16:10',
            'status': 2
        }

    ]
}

conversation2 = {
    'number1': '+91 99999 11111',
    'number2': '+91 99999 33333',
    'messages': [
        {
            'text': 'Python Kaisi Chal Rahi Hai',
            'sender': '+91 99999 11111',
            'timeStamp': '13:55',
            'status': 3
        },
        {
            'text': 'Baki Sab toh Badhiya Hai. recusrion ne he dimaag ghumaya hai',
            'sender': '+91 99999 33333',
            'timeStamp': '17:00',
            'status': 2
        },
        {
            'text': 'Thank you for understanding',
            'sender': '+91 99999 11111',
            'timeStamp': '12:55',
            'status': 3
        }

    ]
}

conversation3 = {
    'number1': '+91 99999 11111',
    'number2': '+91 99999 44444',
    'messages': [
        {
            'text': 'Thank you for understanding',
            'sender': '+91 99999 11111',
            'timeStamp': '12:55',
            'status': 3
        }
    ]
}

my_whatsapp = [conversation1, conversation2, conversation3]


def search_by_sender(phone_number):
    for idx in range(len(my_whatsapp)):
        for idx1 in range(len(my_whatsapp[idx]['messages'])):
            if my_whatsapp[idx]['messages'][idx1]['sender'] == phone_number:
                print(my_whatsapp[idx]['messages'][idx1])
                print("=====================")


def sort_conv():
    n = len(my_whatsapp)
    for idx1 in range(0, n):
        for idx2 in range(0, n-idx1-1):
            if len(my_whatsapp[idx2]['messages']) > len(my_whatsapp[idx2+1]['messages']):
                my_whatsapp[idx2], my_whatsapp[idx2+1] = my_whatsapp[idx2+1], my_whatsapp[idx2]


def filter_conversations():
    for idx in range(len(my_whatsapp)):
        for idx1 in range(len(my_whatsapp[idx]['messages'])):
            print('==========')
            print(my_whatsapp[idx]['messages'][idx1]['text'])
            print(my_whatsapp[idx]['messages'][idx1]['sender'])
            print(my_whatsapp[idx]['messages'][idx1]['timeStamp'])
            if my_whatsapp[idx]['messages'][idx1]['sender'] == 1:
                print('\u2713')
            else:
                print('\u2717')
            print("============================")
            print()


print("Welcome to Whatsapp")
print("===================")

choice = "yes"

while choice == "yes":
    print("1. [search] message by sender")
    print("2. [sort] the conversations based on message length")
    print("3. [filter] the conversations to display only messages or text inside message")
    option = int(input("enter option 1,2 or 3:" ))


    if option == 1:
        print("seach message by sender")
        number = input("enter phone number: ")
        search_by_sender(phone_number=number)

    elif option == 2:
        print("sort conversations based on message length")
        sort_conv()
        print("sorted conversations")
        for idx in range(len(my_whatsapp)):
            print(my_whatsapp[idx])
            print("^^^^^^^^^^^^^^^")
            print()

    elif option == 3:
        print("filter conversations")
        filter_conversations()

    else:
        print("invalid option")

    choice = input("yes to continue no to quit: ")


print("Thank u for using whatsapp")

def max_char():
    for idx in range(len(my_whatsapp)):
        for idx4 in range(len(my_whatsapp[idx]['messages'])):
            if











