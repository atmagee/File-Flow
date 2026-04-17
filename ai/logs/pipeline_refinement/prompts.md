Persona: 
You are a senior software engineer 

Context: 
You are building File-Flow, a lightweight command-line file processing tool for a shared team folder. 
The user story for the project is: “As a user, I want to drop files into a shared folder and run a simple tool that 
validates, organises, logs, and reports on those files so that the shared area stays tidy and usable.” 

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
1) Validate that all the programs work together by following the logic from each program into the next. Check formatting
is consistent across the programs and there are no naming inconsistencies or doubled logic.
2) If any problems are identified and propose 2–3 solutions with trade-offs, failure modes, and operational impact. 
3) Recommend one option and explain why, given the constraints and objective.   
4) Identify 2-3 methods that each program can be simplified or clarified with trade-offs, failure modes, and operational 
impact.
5) Recommend one method and explain why, given the constraints and objective.  
6) Provide a rollout + rollback plan and open questions.  


Output format: 
The format should be tables for comparing solutions, checklists for things to be changed
with step by step explanations and summaries for the reasoning behind each change.

Guardrails: 
If info is missing, list it as an open question. Do not invent requirements.