#!/bin/sh

fnd=$(grep -ri "\bnoqa\b" udaw_test Ud4wTestTask)

if [[ $fnd ]]; then
    echo "WARNING: noqa statements were found"
    exit 1
else
    exit 0
fi
