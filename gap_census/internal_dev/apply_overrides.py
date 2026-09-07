#!/usr/bin/env python3
"""Overlay known in-house AMD-ROS / AMD-cuRobo coverage onto gaps.tsv.

Reads gaps.tsv IN PLACE in this directory (internal_dev/), which is a copy of
the top-level ledger — the top-level gap_census/gaps.tsv is never touched.
"""
import csv

OVERRIDE = {
    "C012": "NITROS-equivalent zero-copy ROS 2 transport already in development in-house",
    "C013": "NITROS-equivalent GPU-memory bridge covered by in-house AMD-ROS effort",
    "C014": "Accelerated component-graph framework covered by in-house AMD-ROS effort",
    "C019": "AprilTag/fiducial detection model already in development in-house",
    "C025": "Depth-based segmentation model already in development in-house",
    "C026": "Semantic image segmentation model already in development in-house",
    "C027": "Freespace segmentation model already in development in-house",
    "C029": "6D pose estimation node already in development in-house",
    "C068": "6D pose estimation foundation model already in development in-house",
    "C051": "cuRobo-equivalent GPU motion planning already in development in-house (AMD-cuRobo)",
    "C052": "cuMotion-equivalent motion generation covered by in-house AMD-cuRobo effort",
    "C053": "MoveIt 2 motion-planning node covered by in-house AMD-cuRobo effort",
    "C312": "Portable GPU motion planning — same in-house AMD-cuRobo effort as C051-C053",
}

path = "gaps.tsv"
rows = list(csv.reader(open(path, newline=""), delimiter="\t"))
header, body = rows[0], rows[1:]

n = 0
for r in body:
    rid = r[0]
    if rid in OVERRIDE:
        r[1] = "partial"                                          # amd_status
        r[2] = "in-house AMD-ROS/AMD-cuRobo equivalent (unpublished)"  # amd_equivalent
        r[3] = "high"                                              # confidence
        r[4] = r[5] = r[6] = r[7] = "-"                            # score axes -> not an open gap
        r[8] = OVERRIDE[rid]                                        # gap_title
        r[11] = "internal:in-house-development"                     # evidence
        n += 1

with open(path, "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n")
    w.writerow(header)
    w.writerows(body)

print(f"overrode {n} rows in {path}")