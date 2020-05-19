#!/usr/bin/env python

import sys

def collapseLines(lines, currentBuild, collapsedLines):
  if not lines: # End of the algorithm.
    return collapsedLines + [currentBuild]
  # We can now assume lines has an element.
  head, *tail = lines # Head will be something, tail may be empty.
  if not currentBuild: # Needed because can't unpack an empty list in python.
    return collapseLines(tail,
                         (head[9], [head]),
                         collapsedLines)
  else:
    id, hits = currentBuild # Can do this because we know it isn't empty.
    if head[9] != id:
      return collapseLines(tail, 
                           (head[9], hits + [head]),
                           collapsedLines + [currentBuild])
    else:
      return collapseLines(tail,
                           (head[9], hits + [head]),
                           collapsedLines)

def alignmentScore(alignmentLine):
  identities = int(alignmentLine[0])
  mismatches = int(alignmentLine[1])
  ns = int(alignmentLine[3])
  qGapCount = int(alignmentLine[4])
  qGapBases = int(alignmentLine[5])
  tGapCount = int(alignmentLine[6])
  tGapBases = int(alignmentLine[7])
  qLength = int(alignmentLine[10])
  bools = [bool(x) for x in [(identities + mismatches + ns + qGapCount) != qLength,
                             tGapCount,
                             qGapCount,
                             ns,
                             mismatches]]
  binaryString = "".join([str(int(x)) for x in bools])
  return int(binaryString,2)

with open(sys.argv[1], "r") as fh:
  lines = [x.strip().split() for x in fh.readlines()]
  collapsed = collapseLines(lines[5:25], [], [])
  for c in collapsed:
    id, alignments = c
    for a in alignments:
      print(id, alignmentScore(a))
