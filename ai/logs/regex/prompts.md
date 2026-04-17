Persona: 
You are a senior software engineer 

Context: 
You are building File-Flow, a lightweight command-line file processing tool for a shared team folder. 
The user story for the project is: “As a user, I want to drop files into a shared folder and run a simple tool that 
validates, organises, logs, and reports on those files so that the shared area stays tidy and usable.” The valid file 
extensions are stored in a file called extensions.txt.

Objective:
The required features are:
* Scan a chosen input folder
* Detect files available for processing
* Validate filenames against a naming convention
* Classify files by type or naming rule
* Move valid files to the correct output folder
* Move invalid files to a quarantine folder
* Generate a text or CSV summary report
* Record actions to a log file
* Support repeated runs without crashing
* Save configuration in a file such as JSON

The deliverables are:
* Git repository
* Python source code
* README.md
* Dockerfile
* One or more Bash scripts
* Sample input files
* Config file
* Log file sample
* Generated report sample
* Short AI usage log
* Short demo presentation

Tasks:
The tasks are to:
1) Create a regex that first validates the files are in the correct format and have a valid filename and extension.
- A valid file name must end in one of those extensions e.g. .txt .pdf .xml are valid.
- A valid file name must be lowercase and start with a word of any length.
- The first word can be followed by either the file extension itself or an underscore followed by another word.
- These words can have a number on the end, but numbers can only be at the end of a filename and must be preceded a word
of any length.


Output format: 
The format of your output should be a README file for use on GitHub, that clearly explains how each part of the criteria 
provided to you is met by the regex as well as examples showing valid and invalid filenames.

Guardrails: 
If info is missing, list it as an open question. Do not invent requirements.

---

Compare the regex you created to the one I created: ^[a-z]+(?:_[a-z]+)*(?:[0-9]+|_[a-z]+[0-9]+)?\.(txt|pdf|xml)$

Provide examples where they are both given a set of valid and invalid filenames, and use a table to compare how they 
handle them. Provide 2-3 positives and negatives for each regex and provide reasoning for why one should be chosen over 
the other as better in any given field and show examples.

The format of the results is a table comparing how robust and accurate they are as well as computational cost. You may
include any other parameters to compare the two that you believe are important as a senior data engineer, but must 
provide reasoning for their inclusion.

---

Create a Markdown AI usage log for this interaction for documentation use as part of the previously specified project

---
