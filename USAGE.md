## How to Use the Email ID Generator

This guide explains, step by step, how to run `main.py` and what to enter at each prompt.

---

## 1. Open the Project Folder in a Terminal

1. On Windows, open **Command Prompt** or **PowerShell**.
2. Navigate to the project directory (adjust the path if needed):

   ```bash
   cd "C:\Users\Hp\Desktop\Email ID Generator"
   ```

3. Make sure `main.py` is inside this folder.

---

## 2. Run the Script

In the same terminal window, run:

```bash
python main.py
```

or, if your system uses `py`:

```bash
py main.py
```

You should see a welcome message like:

```text
Welcome! Dear Sir/Madam
Fill your Details Please
Processing the Data
```

---

## 3. Fill in Your Details

The script will ask you several questions one by one. Type your answer and press **Enter** after each:

1. **Name**

   ```text
   Enter your name:
   ```

   - Example: `JohnDoe`

2. **Age**

   ```text
   Enter your Age:
   ```

   - Example: `25`
   - This must be a number (the script converts it to an integer).

3. **Date of Birth (DOB)**

   ```text
   Enter your DOB:
   ```

   - Example: `01-01-2000` or `1 Jan 2000`
   - The script does not enforce a specific format, but something clear is recommended.

4. **Purpose of the Email**

   ```text
   For what purpose you are making this Email:
   ```

   - Example: `job applications`, `college`, `personal`, etc.

5. **Profession**

   ```text
   Name of your Profession:
   ```

   - Example: `student`, `developer`, `teacher`, etc.

6. **Gender**

   ```text
   Enter your Gender (Male/Female):
   ```

   - Type `Male` or `Female` (case-insensitive).
   - This controls whether the script calls you `Sir` or `Mam` in messages and files.

After this, the program will show some “Saving your Details!” and “Processing” messages with small delays.

---

## 4. Where Do You Want the Email Suggestions?

Next, you will be asked:

```text
You want Email in File or in Terminal:
```

- If you type **`file`** (any case, e.g. `File`, `FILE`):
  - The program **appends** your 4 email suggestions to a text file.
  - The file is named: `<YourName>_<YourProfession>_Email_ID.txt`
  - Example: `JohnDoe_Developer_Email_ID.txt`
  - You will see a confirmation like:

    ```text
    Please Check Your file has been generated Sir
    ```

- If you type anything else (for example `terminal`):
  - The program will print the emails **directly in the terminal**, for example:

    ```text
    Dear Sir,
    We have generate four emails for you choose your and create by your choice

    email 1 = JohnDoe_Developer_123@gmail.com,
    email 2 = ...
    email 3 = ...
    email 4 = ...

    Thanks to use our application, Please visit again!
    ```

---

## 5. Generated Files

On the first run, the script creates a file in the same folder as `main.py`:

- `YourName_YourProfession_Email_ID.txt`

Example:

- `JohnDoe_Developer_Email_ID.txt`

This file will contain:
- Your name, age, DOB, gender, profession, and purpose.
- If you chose `file` for the email output, the script also appends:
  - A small message + 4 suggested email IDs.

You can open this file with:
- Notepad
- VS Code
- Any other text editor

---

## 6. Generating More Email IDs

After completing one full run and showing (or saving) the email IDs, the script asks:

```text
Do you want to generate again! (Yes/No):
```

- If you type **`Yes`** (case-insensitive):
  - The script runs `main()` again.
  - You can enter new details or reuse similar ones.
  - Another set of email suggestions will be generated.

- If you type **anything else**:
  - The script shows a thank-you message and exits:

    ```text
    Thanks to use our code, please visit again!
    ```

---

## 7. Tips & Best Practices

- **Name and profession**: Try using values that look good inside an email ID, for example:
  - `JohnDoe`, `John`, `Jane`, `JDoe`
  - `developer`, `student`, `designer`
- **Purpose**: This is mostly for your reference in the details file, but it can also influence which parts are randomly chosen to form the email.
- **Multiple runs**: Because the script uses randomness, running it multiple times with the same inputs can still produce different email suggestions.
- **Domain**: All suggestions end with `@gmail.com`; you can change this manually later if needed when you create the actual email account.

---

## 8. Troubleshooting

- **Nothing happens when I run `python main.py`**:
  - Make sure you are in the correct folder where `main.py` is located.
  - Check that Python 3 is installed and available on your PATH.

- **`python` command not found**:
  - Try `py main.py` instead of `python main.py`.

- **Script crashes when entering age**:
  - Ensure you are entering only numbers for age (e.g. `25`, not `twenty five`).

If you still face issues, re-check each step in this guide or add more print statements to `main.py` to see what is happening internally.

