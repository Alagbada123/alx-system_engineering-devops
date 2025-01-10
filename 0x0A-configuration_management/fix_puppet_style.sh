#!/bin/bash

# Automatically fix puppet code style issues using puppet-lint and autopep8 (if needed)
for file in *.pp; do
  # Linting the file with puppet-lint
  puppet-lint $file

  # Apply fixes with autopep8 for Python-based files (if necessary)
  if [[ "$file" == *.py ]]; then
    autopep8 --in-place $file
  fi
done

# Optionally, apply additional formatting or fixes for Puppet files
echo "Code formatting completed."

