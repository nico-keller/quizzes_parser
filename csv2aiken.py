import pandas as pd

# Load the dataset
file_path = '/Users/nicolaskeller/Downloads/MAIN ABU 04 Verantwortung übernehmen - 4.02 Mobilität - Vergleich Leasing und Konsumkredit.csv'
data = pd.read_csv(file_path)

# Function to convert CSV data to Aiken format
def convert_to_aiken(df):
    aiken_lines = []

    for index, row in df.iterrows():
        question = row['Question Text']
        answers = [row['Answer'], row['Answer.1'], row['Answer.2'], row['Answer.3']]
        correctness = [row['Is Correct?'], row['Is Correct?.1'], row['Is Correct?.2'], row['Is Correct?.3']]

        # Start the question
        aiken_lines.append(question)

        # Add answers with A/B/C/D labels
        for i, (answer, correct) in enumerate(zip(answers, correctness)):
            label = chr(65 + i)  # Convert 0,1,2,3 to A,B,C,D
            aiken_lines.append(f"{label}. {answer.strip()}")

        # Identify the correct answer(s)
        correct_labels = [chr(65 + i) for i, correct in enumerate(correctness) if correct]
        aiken_lines.append(f"ANSWER: {','.join(correct_labels)}")
        aiken_lines.append("")  # Blank line after each question

    return "\n".join(aiken_lines)

# Convert the data to Aiken format
aiken_output = convert_to_aiken(data)

# Save the output to a .txt file
output_file = '/Users/nicolaskeller/Downloads/questions_in_aiken_format.txt'
with open(output_file, 'w') as f:
    f.write(aiken_output)

print(f"Aiken format file saved to: {output_file}")
