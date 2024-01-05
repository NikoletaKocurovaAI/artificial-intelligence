# How to start

Clone the project.

Create new branch from the main.

## How to name the branch
The naming convention for each branch follows a structured format, incorporating the project name in capital letters, 
followed by the task number, and concluding with the task name in lowercase letters.

Example:

`AI-task2-dummy-unit-test-to-run-in-github-pipeline`

# Code style

## Formatting

For Python files, the black is used.

Example:

`black --check computer-vision/robot-object-recognition/src/python/frontend_app`

`black computer-vision/robot-object-recognition/src/python/frontend_app`

# Commit Message Guidelines

## Format

Each commit message consists of the type (such as feat, refactor, ...), scope, task number and message text.

## Type

- feat: New feature.
- refactor: A code change that is not feature.
- style: Formatting.
- test: Tests.
- docs: Documentation.
- ci: Changes to the workflows configuration files (.github/workflows).

## Scope

- Artificial Intelligence (AI)
- Computer Vision (CV)
- Robot Object Recognition (ROR)
  - frontend-app
  - model
  - status-api
  - model-api

**Example:**

`git add .`

`git commit -m "refactor(ror/frontend-app): Task5 Moving the app to src/python directory, so the black can be run on it."`

`git push`
