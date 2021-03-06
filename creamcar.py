#!/usr/bin/env python

import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", type=str,
                    help="input file",
                    required=True)
parser.add_argument("--print-top-scoring-alignment",
                    help="print top scoring alignment from blat",
                    action="store_true",
                    default=False)
parser.add_argument("--suppress-top-scoring-category",
                    help="do not print category of top scoring alignment from blat",
                    action="store_true",
                    default=False)
args = parser.parse_args()

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
  head, *tail = lines # Unpack lines.
  currentBuild = [head]
  idNow = head[9] # 10th column is query ID.
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
  # Convert a line of blat output into a human-readable description.
  identities = int(alignmentLine[0])
  mismatches = int(alignmentLine[1])
  ns         = int(alignmentLine[3])
  qGapCount  = int(alignmentLine[4])
  qGapBases  = int(alignmentLine[5])
  tGapCount  = int(alignmentLine[6])
  tGapBases  = int(alignmentLine[7])
  qLength    = int(alignmentLine[10])
  isNotFullLength = ((identities + mismatches + ns + qGapBases) != qLength)
  bools = [bool(x) for x in [isNotFullLength, # Worst case.
                             tGapCount,
                             qGapCount,
                             ns,
                             mismatches]]     # Best case.
  binaryString = "".join([str(int(x)) for x in bools])
  return int(binaryString,2)

def mapScoreToMeaning(score):
  meaning = []
  binary = [bool(int(x)) for x in list(str(bin(score))[2:].zfill(5))]
  if binary[0]:
    meaning += ["not full-length"]
  else:
    meaning += ["full-length"]
  if binary[1]:
    meaning += ["tGaps"]
  if binary[2]:
    meaning += ["qGaps"]
  if binary[3]:
    meaning += ["Ns"]
  if binary[4]:
    meaning += ["mismatches"]
  return " with ".join(meaning)

if (not args.print_top_scoring_alignment) and args.suppress_top_scoring_category:
  print("I need to print something!")
else:
  print(args.print_top_scoring_alignment, args.suppress_top_scoring_category)
  with open(args.file, "r") as fh:
    lines = [x.strip().split() for x in fh.readlines()]
    collapsed = collapseLinesP(lines[5:])
    for c in collapsed:
      id, alignments = c
      scores = [[alignmentScore(a),a] for a in alignments]
      topScore = sorted(scores, key=lambda x: int(x[0]))[0]
      if args.print_top_scoring_alignment:
        print("\t".join(topScore[1]))
      if not args.suppress_top_scoring_category:
        print(id, mapScoreToMeaning(topScore[0]))
