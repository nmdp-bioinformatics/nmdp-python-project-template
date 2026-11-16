#!/bin/sh

# SPDX-FileCopyrightText: 2026 (NMDP) National Marrow Donor Program. All Rights Reserved.
#
# SPDX-License-Identifier: LGPL-3.0-or-later

set -e

# A positive integer generally in the 2-4 x $(NUM_CORES) range.
WORKER_PROCESSES=${WORKERS:-4}

echo "Starting service with" "${WORKER_PROCESSES}" worker processes.

if [ "${WORKER_PROCESSES}" != "1" ]; then
  WORKER_FLAG="--workers=${WORKER_PROCESSES}"
fi

# shellcheck disable=SC2086
python3 /app/.venv/bin/gunicorn -c gunicorn_config.py ${WORKER_FLAG} app:app
