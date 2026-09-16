# To construct the Semicolon-Delimited to Comma-Delimited assignment, I typed the following code:

  ```bash

# $1 takes the file passed as an argument
input_file="$1"

# Creates output file
output_file="${input_file%.*}_converted.csv"

# Replace semicolons with commas, write out new files
tr ';' ',' < "$input_file" > "$output_file"

echo "Converted $input_file and saved as $output_file"

# This code can run with the function "Bash Clark_Semicolon_Converter.sh Pacifici2013_data.csv"
# TO perform bring the code to the remote repository, I performed the following functions:

git add Clark_Semicolon_Converter.sh
git commit -m "Added Clark_Semicolon_Converter.sh"
git push origin main --force

``
