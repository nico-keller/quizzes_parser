import pandas as pd

# Function to convert CSV data to Aiken format
def convert_to_aiken(df):
    aiken_lines = []

    for index, row in df.iterrows():
        # Skip rows with missing question text
        if pd.isna(row.get('Question Text')):
            continue

        # Extract the question text
        question = row['Question Text'].strip()
        aiken_lines.append(question)

        # Process answers and correctness
        correct_labels = []
        for i in range(4):  # Assuming four possible answers
            answer_col = f'Answer.{i}' if i > 0 else 'Answer'
            correct_col = f'Is Correct?.{i}' if i > 0 else 'Is Correct'

            if answer_col in df.columns and correct_col in df.columns:
                # Check if the answer exists and is not empty
                if pd.notna(row[answer_col]):
                    answer = row[answer_col].strip()
                    label = chr(65 + i)  # Convert 0,1,2,3 to A,B,C,D
                    aiken_lines.append(f"{label}. {answer}")

                    # Check correctness
                    if str(row[correct_col]).strip().lower() in ['true', '1']:
                        correct_labels.append(label)

        # Add correct answer(s) to the output
        if correct_labels:
            aiken_lines.append(f"ANSWER: {','.join(correct_labels)}")
        aiken_lines.append("")  # Blank line after each question

    return "\n".join(aiken_lines)

# Load the dataset
file_path = '/Users/nicolaskeller/Downloads/MAIN ABU 04 Verantwortung übernehmen - 4.02 Mobilität - Vergleich Leasing und Konsumkredit.csv'
data = pd.read_csv(file_path)

# Convert the data to Aiken format
aiken_output = convert_to_aiken(data)

# Save the output to a .txt file with dynamic naming
output_file = file_path.replace('.csv', '_aiken.txt')
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(aiken_output)

print(f"Aiken format file saved to: {output_file}")
