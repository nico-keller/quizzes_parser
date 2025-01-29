import pandas as pd

def csv_to_gift(csv_path, output_path):
    # Load CSV data
    df = pd.read_csv(csv_path)

    # Open a file for writing the GIFT output
    with open(output_path, 'w', encoding='utf-8') as gift_file:
        for index, row in df.iterrows():
            # Skip rows with missing question text
            if pd.isna(row['Question Text']):
                continue

            # Write the question
            question_text = row['Question Text'].strip()
            gift_file.write(f"::Q{index + 1}::{question_text} {{\n")

            # Process each answer column and its correctness
            for i in range(4):  # Assuming four possible answers
                answer_col = f'Answer.{i}' if i > 0 else 'Answer'
                correct_col = f'Is Correct?.{i}' if i > 0 else 'Is Correct'

                if answer_col in df.columns and correct_col in df.columns:
                    # Check if the answer exists and is not empty
                    if pd.notna(row[answer_col]):
                        answer = row[answer_col].strip()
                        correctness = "=" if str(row[correct_col]).strip().lower() in ['true', '1'] else "~"
                        gift_file.write(f"    {correctness} {answer}\n")

            # Close the question block
            gift_file.write("}\n\n")

# Define paths for input and output
file_path = '/Users/nicolaskeller/Downloads/MAIN ABU 04 Verantwortung übernehmen - 4.02 Mobilität - Vergleich Leasing und Konsumkredit.csv'
output_path = file_path.replace('.csv', '_gift.txt')

# Convert CSV to GIFT
csv_to_gift(file_path, output_path)
