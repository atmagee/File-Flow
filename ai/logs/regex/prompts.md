You are a senior data engineer.

The context is that you have been tasked with sorting the files in a shared team folder by creating an easy to run tool
using Python. The valid file type extensions are stored in a file called "extensions.txt".

Your task is to create a regex that first validates the files are in the correct format and have a valid type. A valid
file name must end in one of those extensions e.g. .txt .pdf .xml are valid. A valid file name must also all be
lowercase and start with a word of any length but can be followed by either the extension itself or an underscore
preceding another word. These words can have a number on the end, but numbers can only be at the end of a filename and
must be preceded a word of any length.

The format of your output should be a README file for use on GitHub, that clearly explains how each part of the criteria
I provided to you is met with the regex as well as examples showing valid and invalid filenames.

---

Can you compare the regex you created to this one ^[a-z]+(?:_[a-z]+)*(?:[0-9]+|_[a-z]+[0-9]+)?\.(txt|pdf|xml)$

Give the results in the form of a table comparing how robust and accurate they are as well as computational cost and any
other parameters you believe are important as a senior data engineer. Provide reasoning for which one is chosen as
better in any given field and show examples.

---

Create me a Markdown AI usage log for this interaction for documentation use as part of the previously specified project

---

Create a section for a GitHub ReadMe file that explains the reasoning for why the final regex was chosen and provide
clear example of valid and invalid file names in the form of tables and lists.