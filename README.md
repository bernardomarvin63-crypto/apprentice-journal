# Apprentice Journal

This repository tracks my journey from Information Systems graduate to full stack software developer specializing in business systems.

## Day 1 — Foundation Setup

Today I set up my development environment from scratch:

- Installed WSL2 with Ubuntu on Windows
- Configured Git with my identity
- Generated SSH keys and connected to GitHub
- Installed VS Code with the WSL extension
- Created this repository

This is more than installation — it's the foundation every line of code I write from here will live on.

## Day 2 — Day 1 Review

May 28, 2026, today, I reviewed everything I was taught and went deeper with the previous lessons including all the errors I made.

## Day 3 — Day 1 Review and More

May 29, 2026, today, I did what I did yesterday and read the article “What is Version Control?” from Atlassian.com. I will re-read it tomorrow, and I may also re-read it tonight.

## Day 4 — Meaning and Importance of Version Control

June 02, 2026, today, I went in depth with version control systems and why is it important for software developers. What is Git and GitHub while it was confusing at first I found out that Git is the version control system that runs locally on your computer and GitHub is the hosting service for your Git projects. Git and GitHub allows me to track changes in project/source code where for obvious reasons is super important when developing software projects, especially when your working with others.

## Weekly Synthesis

What is Git actually doing under the hood?
Under the hood, Git manages your project as a directed acyclic graph (DAG) of snapshots, rather than tracking individual file differences. When you make a commit, Git takes the current state of your files, compresses them into unique data objects called "blobs," organizes them into a directory structure called a "tree," and links them to a "commit" object that points to its parent commits. Because each object is named using a unique cryptographic hash (SHA-1 or SHA-256) based strictly on its contents, Git ensures absolute data integrity; if a single byte of your code changes, its hash changes, allowing Git to track the entire history of your codebase efficiently through content-addressable storage.

Why SSH Matters?
SSH (Secure Shell) matters because it provides a secure, encrypted channel for your computer to communicate with remote servers like GitHub without exposing your passwords. By using a pair of cryptographic keys (a public one shared with GitHub and a private one kept secret on your machine), it automates authentication for every push and pull. This setup keeps your code transfers safe from interception while sparing you from constantly typing in login credentials.

What was the hardest part of this week?
To be honest, the hardest part of this week is being consistent, which I understand is the key to what I am trying to achieve. The terminologies, the syntax, the process, the definitions, all of this I can re-read where I learn the most but dedicating time everyday is very hard for now due to my job workload. 

What do I still not fully understand?
Linux, I'm a windows user ever since I started using a computer so the operating system is new to me.