import pandas as pd

# Load the CSV file to examine its structure
file_path = '/Users/nicolaskeller/Downloads/MAIN ABU 04 Verantwortung übernehmen - 4.02 Mobilität - Vergleich Leasing und Konsumkredit.csv'
csv_data = pd.read_csv(file_path)

# Display the first few rows to understand its structure
csv_data.head()


def csv_to_gift(csv_path, output_path):
    # Load CSV data
    df = pd.read_csv(csv_path)

    # Open a file for writing the GIFT output
    with open(output_path, 'w', encoding='utf-8') as gift_file:
        for index, row in df.iterrows():
            # Write the question
            question_text = row['Question Text']
            gift_file.write(f"::Q{index + 1}::{question_text} {{\n")

            # Process each answer column and its correctness
            for i in range(4):  # Assuming four possible answers
                answer_col = f'Answer.{i}' if i > 0 else 'Answer'
                correct_col = f'Is Correct?.{i}' if i > 0 else 'Is Correct?'

                # Check if the answer exists and is not empty
                if pd.notna(row[answer_col]):
                    answer = row[answer_col].strip()
                    correctness = "=" if row[correct_col] else "~"
                    gift_file.write(f"    {correctness} {answer}\n")

            # Close the question block
            gift_file.write("}\n\n")

# Define paths for input and output
output_path = '/Users/nicolaskeller/Downloads/gift_format.txt'
# Convert CSV to GIFT
csv_to_gift(file_path, output_path)


