#!/bin/bash

# Run the second script
/usr/bin/python3 /app/run_app.py &

# Run the first script
/usr/bin/python3 /app/llm_code_to_check_description/main.py &

# Wait for all background jobs to finish
wait
