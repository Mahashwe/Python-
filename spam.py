def spam(emails):
    spam_words = ['win', 'free', 'cash', 'hurry', 'discount', 'luckydraw']
    email_words = emails.split()  # Split the email into a list of words
    
    for word in email_words:  # Iterate through each word in the list
        if word.lower() in spam_words:  # Convert the word to lowercase for case-insensitive comparison
            print("SPAM:", emails)
            break
    else:
        print("NOT SPAM:", emails)

with open('mail.txt','r') as file:
    emails = file.read()
spam(emails)
