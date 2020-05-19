#!/usr/bin/env python

import sys

def collapseLinesF(lines, currentBuild, collapsedLines):
  # Functional version.
  # NOTE: Does not work since Python does not support tail recursion.
  if not lines: # End of the algorithm.
    return collapsedLines + [currentBuild]
  # We can now assume lines has an element.
  head, *tail = lines # Head will be something, tail may be empty.
  if not currentBuild: # Needed because can't unpack an empty list in python.
    return collapseLinesF(tail,
                         (head[9], [head]),
                         collapsedLines)
  else:
    id, hits = currentBuild # Can do this because we know it isn't empty.
    if head[9] != id:
      return collapseLinesF(tail, 
                           (head[9], hits + [head]),
                           collapsedLines + [currentBuild])
    else:
      return collapseLinesF(tail,
                           (head[9], hits + [head]),
                           collapsedLines)

def collapseLinesP(lines):
  # Iterative version.
  if not lines:
    return []
  collapsedLines = []
  head, *tail = lines
  currentBuild = [head]
  idNow = head[9]
  head, *tail = tail
  while tail:
    if head[9] != idNow:
      collapsedLines += [(idNow, currentBuild)]
      currentBuild = [head]
      idNow = head[9]
    else:
      currentBuild += [head]
    head, *tail = tail
  if head[9] == idNow:
    collapsedLines += [(idNow, currentBuild + [head])]
  else:
    collapsedLines += ([(idNow, currentBuild)] + [(head[9], [head])])
  return collapsedLines

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
  collapsed = collapseLinesP(lines[5:])
  for c in collapsed:
    id, alignments = c
    for a in alignments:
      print(id, alignmentScore(a))
