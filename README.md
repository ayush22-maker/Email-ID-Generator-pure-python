## Email ID Generator / Suggester

This is a simple **console-based Python application** that helps you generate suggested email IDs based on your personal details and a bit of randomness.

The script:
- Asks you for some basic details (name, age, DOB, profession, gender, and purpose of the email).
- Saves your details in a text file.
- Randomly combines parts of your details with a random number to generate email suggestions.
- Lets you choose whether to see the generated email IDs directly in the terminal or append them to your details file.

---

## Features

- **Interactive prompts** for all required details.
- **Gender-aware salutation** (`Sir` / `Mam`) in messages and output.
- **Automatic details file** named like `YourName_YourProfession_Email_ID.txt`.
- **Randomized email suggestions** using your details plus a random number (1–999).
- **Multiple suggestions at once** (4 email suggestions per run).
- **Option to re-run** the generator again without restarting the script.

---

## Project Structure

- `main.py` – main Python script containing all the logic and user interaction.
- `README.md` – overview and project documentation (this file).
- `USAGE.md` – step-by-step instructions for running and using the script.
- `*_Email_ID.txt` – generated per user run, storing your details and (optionally) your email suggestions.

---

## Requirements

- **Python**: Version 3.x (any fairly recent Python 3 should work).
- **OS**: Works on Windows, macOS, and Linux (script is console-based).
- **Modules used**: Only standard library modules:
  - `random`
  - `time`

No extra packages are required beyond a standard Python 3 installation.

---

## How It Works (High-Level)

1. The script greets you and shows some "processing" delays for a nicer experience.
2. The `main()` function:
   - Prompts for:
     - Name
     - Age
     - Date of Birth (free text, e.g. `01-01-2000`)
     - Purpose of the email (e.g. `job applications`, `personal`, `college`, etc.)
     - Profession (e.g. `student`, `developer`, `teacher`)
     - Gender (`Male` or `Female`)
   - Sets `Sir` or `Mam` according to your gender.
   - Creates a details file named `<Name>_<Profession>_Email_ID.txt` and writes all your details to it.
   - Builds a list of your inputs and chooses random elements from it to form the start and end of the email.
   - Picks a random number between 1 and 999.
   - Generates 4 email suggestions with the pattern:
     - `<StartPart>_<EndPart>_<Number>@gmail.com`
   - Asks whether you want the emails in a **file** or in the **terminal**.
     - If `file`: the 4 email suggestions are appended to your details file.
     - Otherwise: the 4 suggestions are printed in the terminal.
3. After the first run, the script asks if you want to generate again.
   - If you answer `Yes` (case-insensitive), `main()` runs again.
   - Otherwise, the script thanks you and exits.

For more detailed, step-by-step usage instructions (with example runs), see `USAGE.md`.

---

## Running the Script

1. **Open a terminal** (Command Prompt, PowerShell, or any terminal).
2. **Navigate to the project folder**:

   ```bash
   cd "C:\Users\Hp\Desktop\Email ID Generator"
   ```

3. **Run the script with Python**:

   ```bash
   python main.py
   ```

   or, depending on your setup:

   ```bash
   py main.py
   ```

4. **Follow the prompts** in the terminal to enter your details and choose how you want to see the generated email IDs.

---

## Example Output Files

After one successful run, you will see a file similar to:

- `YourName_YourProfession_Email_ID.txt`

This file will contain:
- Your saved details.
- (Optionally) the 4 email ID suggestions if you chose the `file` option.

You can open this file with any text editor (Notepad, VS Code, etc.).

---

## Notes and Limitations

- The script always uses the `@gmail.com` domain for suggestions.
- Suggested email IDs are **not checked** against real email providers for availability.
- Inputs like DOB and profession are treated as free text and used as-is in the generated email parts.
- Because suggestions use random choices, running the script multiple times with the same details can still produce different results.

---

## Future Improvements (Ideas)

- Allow user to choose the email domain (e.g. `@outlook.com`, `@yahoo.com`).
- Add validation to ensure numeric age, sensible DOB format, etc.
- Offer more structured patterns for email IDs (e.g. `firstname.lastnameYYYY`, etc.).
- Provide an option to generate more (or fewer) than 4 suggestions.

---

## License

This is a personal/small utility script. You can freely modify and use it for learning or personal use. If you publish it or build on top of it, consider giving credit to the original author.

