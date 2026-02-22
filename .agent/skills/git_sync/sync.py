#!/usr/bin/env python3
import subprocess
import sys
import argparse
import os

def run_command(command, dry_run=False):
    print(f"Executing: {' '.join(command)}")
    if dry_run:
        return True, "Dry run enabled. Command skipped."
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr

def main():
    parser = argparse.ArgumentParser(description="Git Sync Agent - Parallel Commit & Push")
    parser.add_argument("-m", "--message", help="Commit message", default="Autosync: Progress update from agent")
    parser.add_argument("--dry-run", action="store_true", help="Show commands without executing")
    parser.add_argument("--pull", action="store_true", help="Pull before pushing", default=True)
    parser.add_argument("--add-all", action="store_true", help="Add all changes", default=True)
    
    args = parser.parse_args()

    # 1. Git Add
    if args.add_all:
        success, output = run_command(["git", "add", "."], args.dry_run)
        if not success:
            print(f"Error adding files: {output}")
            sys.exit(1)

    # 2. Check for changes
    if not args.dry_run:
        res = subprocess.run(["git", "diff", "--cached", "--quiet"])
        if res.returncode == 0:
            print("No changes to commit.")
            sys.exit(0)

    # 3. Git Commit
    success, output = run_command(["git", "commit", "-m", args.message], args.dry_run)
    if not success:
        print(f"Error committing: {output}")
        sys.exit(1)

    # 4. Git Pull (optional but recommended)
    if args.pull:
        success, output = run_command(["git", "pull", "--rebase"], args.dry_run)
        if not success:
            print(f"Error pulling: {output}")
            # We don't exit here as there might be no remote or nothing to pull
            # but usually we want this to succeed if we're pushing.

    # 5. Git Push
    success, output = run_command(["git", "push"], args.dry_run)
    if not success:
        print(f"Error pushing: {output}")
        sys.exit(1)

    print("Successfully synchronized workspace.")

if __name__ == "__main__":
    main()
