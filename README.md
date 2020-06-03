# creamcar
Assigns a class to alignments made with the blat alignment tool (http://www.kentinformatics.com/).

For example it converts the following lines of blat output for a given sequence:

```
8712    33      0       0       2       13      1       6       +       TraesCS1A02G428900.genomic      8758    0       8758    Chr1A   598636984       586868637       586877388       3       4528,2715,1502, 0,4540,7256,    586868637,586873171,586875886,
7460    76      0       0       8       75      9       178     +       TraesCS1A02G428900.genomic      8758    371     7982    Chr1A   598636984       501546808       501554522       14      338,3430,264,52,127,568,22,238,243,163,750,616,447,278, 371,730,4163,4450,4514,4641,5209,5231,5471,5714,5877,6639,7256,7704,      501546808,501547146,501550577,501550891,501550943,501551157,501551730,501551754,501551993,501552237,501552429,501553179,501553795,501554244,
7443    67      0       0       8       105     6       91      +       TraesCS1A02G428900.genomic      8758    370     7985    Chr1A   598636984       522990743       522998344       13      339,1544,2131,52,22,99,562,22,238,406,750,985,360,      370,751,2296,4450,4514,4548,4647,5209,5231,5471,5877,6639,7625,   522990743,522991082,522992626,522994807,522994859,522994881,522994983,522995550,522995574,522995813,522996249,522996999,522997984,
308     2       0       0       1       3       0       0       -       TraesCS1A02G428900.genomic      8758    7682    7995    Chr1A   598636984       586869002       586869312       2       6,304,  763,772,        586869002,586869008,
302     2       0       0       0       0       0       0       -       TraesCS1A02G428900.genomic      8758    7682    7986    Chr1A   598636984       522990744       522991048       1       304,    772,    522990744,
301     3       0       0       0       0       0       0       -       TraesCS1A02G428900.genomic      8758    7682    7986    Chr1A   598636984       501546808       501547112       1       304,    772,    501546808,
283     10      0       0       2       12      1       14      -       TraesCS1A02G428900.genomic      8758    7680    7985    Chr1A   598636984       320954149       320954456       3       232,43,18,      773,1016,1060,  320954149,320954395,320954438,
308     2       0       0       0       0       1       3       -       TraesCS1A02G428900.genomic      8758    365     675     Chr1A   598636984       586876312       586876625       2       304,6,  8083,8387,      586876312,586876619,
301     2       0       0       0       0       0       0       -       TraesCS1A02G428900.genomic      8758    372     675     Chr1A   598636984       522998041       522998344       1       303,    8083,   522998041,
294     5       0       0       1       1       1       2       -       TraesCS1A02G428900.genomic      8758    375     675     Chr1A   598636984       501554221       501554522       2       21,278, 8083,8105,      501554221,501554244,
```
To:

```
TraesCS1A02G428900.genomic full-length with tGaps with qGaps with mismatches
```
Where the alignment class reported is the "best". Applied to a full alignment we can summarise the cases:

```
> python ~/dev/creamcar/creamcar.py IWGSC_v1.1_to_v2.0.genomic.notPerfectMatch.1A.psl|cut -d ' ' -f2-|sort|uniq -c|sort -k1,1nr
    203 full-length with tGaps with qGaps with mismatches
    147 full-length with tGaps with qGaps
    123 full-length with Ns
    114 full-length with mismatches
     37 full-length with qGaps
     36 full-length with qGaps with mismatches
     24 full-length with tGaps with mismatches
     15 not full-length with tGaps with qGaps with mismatches
     13 not full-length
      7 not full-length with mismatches
      5 full-length with tGaps
      4 full-length with Ns with mismatches
      4 full-length with tGaps with qGaps with Ns with mismatches
      3 not full-length with qGaps with mismatches
      2 full-length with tGaps with qGaps with Ns
      2 not full-length with tGaps with qGaps
      1 full-length with qGaps with Ns with mismatches
      1 not full-length with qGaps
      1 not full-length with tGaps with mismatches
```
