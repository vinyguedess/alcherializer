#!/bin/bash

# Install dependencies
deps() {
    pip install -r requirements.txt

    if test -f "/workspace/requirements.test.txt"; then
        pip install -r requirements.test.txt
    fi

    # Allow user installing local dependencies without interfering
    # with production code
    if test -f "/workspace/requirements.local.txt"; then
        pip install -r requirements.local.txt
    fi
}

## Execute command
$1 $@
