# creamcar
Assigns a class to alignments made with blat alignment tool.

For example it converts the following lines of blat output:

```
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
