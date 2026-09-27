# New fast matrix multiplication schemes

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22943995.svg)](https://doi.org/10.5281/zenodo.22943995)

Bilinear schemes for multiplying an n1×n2 matrix by an n2×n3 matrix, all with coefficients in {-1, 0, 1} (ZT), which makes them valid over any ring.

Previous values are the lower of the [FastMatrixMultiplication](https://github.com/dronperminov/FastMatrixMultiplication) table as of 2026-09-26 and the [Sedoglavic catalogue](https://fmm.univ-lille.fr/) as of 2026-09-27.

## Below the best known rank in any ring

| Format | Rank | Previous best (any ring) | Previous ZT |
|---|---|---|---|
| 11×13×15 | **1364** | 1371 | 1377 |
| 11×14×14 | **1373** | 1376 | 1376 |

## Equal to the best known rank, first with ZT coefficients

| Format | Rank | Previous best (any ring) | Previous ZT |
|---|---|---|---|
| 7×7×9 | **315** | 315 | 316 |

## New ZT records

| Format | Rank | Previous ZT | Best known (any ring) |
|---|---|---|---|
| 2×12×15 | 280 | 281 | 278 |
| 2×13×15 | 304 | 305 | 300 |
| 2×13×16 | 324 | 325 | 320 |
| 2×14×16 | 348 | 350 | 344 |
| 2×15×16 | 374 | 375 | 368 |
| 4×11×15 | 457 | 458 | 449 |
| 6×11×11 | 492 | 496 | 490 |
| 7×9×14 | 599 | 600 | 597 |
| 6×11×14 | 617 | 621 | 613 |
| 7×9×15 | 638 | 639 | 634 |
| 9×11×13 | 840 | 843 | 835 |
| 8×11×16 | 906 | 914 | 904 |
| 9×14×16 | 1260 | 1270 | 1254 |
| 9×15×15 | 1269 | 1276 | 1236 |
| 8×16×16 | 1256 | 1260 | 1230 |
| 12×12×15 | 1326 | 1332 | 1280 |
| 10×14×16 | 1416 | 1418 | 1398 |
| 12×13×15 | 1464 | 1470 | 1442 |
| 11×15×15 | 1547 | 1548 | 1540 |
| 11×15×16 | 1641 | 1657 | 1605 |
| 11×16×16 | 1749 | 1752 | 1724 |
| 13×14×16 | 1806 | 1820 | 1796 |

## Files

`schemes/` holds one file per scheme in the JSON format of the FastMatrixMultiplication repository: `n`, `m`, `u`, `v`, `w` and the readable `multiplications` and `elements`; `complexity` is the naive addition count. `SHA256SUMS` lists the checksum of every file.

## Verification

Every scheme satisfies the Brent equations exactly:

```
python verify.py schemes/*.json
```

`verify.py` uses exact rational arithmetic and nothing but the Python standard library. The schemes were also accepted by `validate_schemes` from [ternary_flip_graph](https://github.com/dronperminov/ternary_flip_graph).

## License and citation

The schemes are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please cite as described in `CITATION.cff`.
