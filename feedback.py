feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya',
             'Arjun', 'Kiran', 'Leela', 'Nisha'],
    'Feedback': [
        '   Very GOOD Service!!!',
        'poor support,        not happy   ',
        'GREAT experience! will come again.',
        'okay     okay...',
        '   not    BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],
    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}

# Step 2: Add More Feedbacks

n = int(input("How many feedbacks do you want to add? "))

for i in range(n):
    print("\nEnter feedback details:")

    name = input("Enter Name: ")
    feedback = input("Enter Feedback: ")

    rating = int(input("Enter Rating (1-5): "))

    while rating < 1 or rating > 5:
        print("Rating must be between 1 and 5")
        rating = int(input("Enter Rating (1-5): "))

    feedback_data['S_No'].append(len(feedback_data['S_No']) + 1)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['Rating'].append(rating)


# Step 3: Text Cleaning

cleaned_feedback = []

for feedback in feedback_data['Feedback']:

    feedback = feedback.replace('.', '')
    feedback = feedback.replace(',', '')
    feedback = feedback.replace('!', '')
    feedback = feedback.replace('?', '')

    feedback = ' '.join(feedback.split())

    feedback = feedback.lower()

    cleaned_feedback.append(feedback)

feedback_data['Feedback'] = cleaned_feedback


# Step 4: Word Count Insights

def count_word_in_feedbacks(word):

    count = 0

    for feedback in feedback_data['Feedback']:

        if word.lower() in feedback.split():
            count += 1

    return count


print("\nWord Count Insights")

print("Good:", count_word_in_feedbacks("good"))
print("Poor:", count_word_in_feedbacks("poor"))
print("Excellent:", count_word_in_feedbacks("excellent"))


# Step 5: Final Summary and Insights

print("\nFinal Cleaned Feedback Data")

print(feedback_data)


# Average Rating

average_rating = sum(feedback_data['Rating']) / len(feedback_data['Rating'])

print("\nAverage Rating:", round(average_rating, 2))


# Longest Feedback

longest_feedback = max(
    feedback_data['Feedback'],
    key=lambda x: len(x.split())
)

print("\nLongest Feedback:")
print(longest_feedback)

print("Word Count:", len(longest_feedback.split()))


# Unique Words

unique_words = set()

for feedback in feedback_data['Feedback']:
    words = feedback.split()
    unique_words.update(words)

print("\nUnique Words:")
print(sorted(unique_words))


# Optional: Sort Feedbacks by Rating

sorted_feedbacks = sorted(
    zip(
        feedback_data['S_No'],
        feedback_data['Name'],
        feedback_data['Feedback'],
        feedback_data['Rating']
    ),
    key=lambda x: x[3],
    reverse=True
)

print("\nFeedbacks Sorted by Rating (Highest to Lowest)")

for item in sorted_feedbacks:
    print(item)