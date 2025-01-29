import pandas as pd

# Load the dataset
file_path = '/Users/nicolaskeller/Downloads/MAIN ABU 04 Verantwortung übernehmen - 4.02 Mobilität - Vergleich Leasing und Konsumkredit.csv'
data = pd.read_csv(file_path)


# Function to convert CSV data to Moodle XML format
def convert_to_moodle_xml(df):
    xml_lines = ["<?xml version='1.0' encoding='UTF-8'?>", "<quiz>"]

    for index, row in df.iterrows():
        question = row['Question Text']
        answers = [row['Answer'], row['Answer.1'], row['Answer.2'], row['Answer.3']]
        correctness = [row['Is Correct?'], row['Is Correct?.1'], row['Is Correct?.2'], row['Is Correct?.3']]

        # Add question tag
        xml_lines.append("  <question type=\"multichoice\">")
        xml_lines.append(f"    <name><text>Question {index + 1}</text></name>")
        xml_lines.append(f"    <questiontext format=\"html\"><text><![CDATA[{question}]]></text></questiontext>")
        xml_lines.append("    <answerfraction=" + f"{int(correctness[0]) * 100}" + f">\n")

        # Add answer options
        for i, (answer, correct) in enumerate(zip(answers, correctness)):
            fraction = "100" if correct else "0"
            xml_lines.append(f"    <answer fraction=\"{fraction}\">")
            xml_lines.append(f"      <text><![CDATA[{answer.strip()}]]></text>")
            xml_lines.append("    </answer>")

        # Close question tag
        xml_lines.append("  </question>")

    xml_lines.append("</quiz>")
    return "\n".join(xml_lines)


# Convert the data to Moodle XML format
moodle_xml_output = convert_to_moodle_xml(data)

# Save the output to a .xml file
output_file = '/Users/nicolaskeller/Downloads/questions_in_moodle_format.xml'
with open(output_file, 'w') as f:
    f.write(moodle_xml_output)

print(f"Moodle XML format file saved to: {output_file}")
