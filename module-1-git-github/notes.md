# Module 1 — Git & GitHub

**Student:** John Brian O. Pecson
**Date:** 9/25/26

---

## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)

[Write your own explanation here. What problem does Git actually solve? How is GitHub different from Git itself?]

- Git is like the tool, it's like the save/load function in a game. Git saves you from losing your own project or progress. GitHub is like a place where a lot of projects exist, and here you can make your own repository to store your own project, saving your work applies here too. Git and GitHub differs from a tool and a place to store repositories.

---

## Key vocabulary (in your own words)

- repository: personal project space that you can manage
- commit: commits and prepares the changes to be pushed into the repository
- branch: a branch is like a copy of the main one, this basically allows you to make changes and commits without affecting the main branch and messing something up
- push / pull: push is uploading your changes and commits into its repository, while pull lets you receive the changes into your local repository
- pull request: this is basically a permission to commit and merge changes from another branch into the main branch
- merge conflict: this happens when two changes has the same exact changes and Git basically don't know which change to push or to upload into the main branch

---

## Walking through what I did

[Describe, step by step, a real branch → commit → push → PR you did. Include the actual commands you used.]
- First I made some changes in notes.md and I plan to make the branch on GitHub instead but I did it here in Bash instead, and then I made my git status, git branch then made my branch by doing git branch module1 then committing and pushing it afterwards.

```
# git status, branch, git branch module1, git switch module1, git add module-1-git-github/notes.md, git commit, git push
```

---

## A mistake I made (or one I want to avoid)

[What tripped you up? A confusing error message, committing to the wrong branch, a merge conflict — explain it so a classmate reading this avoids the same mistake.]
- When I was making another branch by using the terminal, I was trying to do it by stock knowledge and I did git branch module1 but I didn't know I could just do git switch -c module1 to instantly create and switch branch
---

## How this connects to something else

[Optional: how does version control relate to anything else you've learned or used before?]
