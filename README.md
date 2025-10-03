# Retail Sales Dashboard

This repository stores scripts and notes for the Retail Sales Dashboard (Power BI internship task).

## Structure
- `power_query/` - Power Query M scripts (paste into Advanced Editor).
- `dax/` - DAX scripts for Calendar table and measures.
- `pbix/` - Optional: place Power BI report files here (use Git LFS if committing).
- `data/` - Data description (don't commit private raw data).
- `docs/` - Visual mockups and documentation.

## Quickstart
1. Import your raw dataset into Power BI as `raw_retail_source`.
2. Create a `cleaned_retail` query and paste `power_query/cleaned_retail.m`.
3. Create the `Calendar` table and measures from `dax/calendar_and_measures.dax`.
4. Build visuals in Report view as documented.

## Notes
- Avoid committing raw data (place instructions or a sample CSV if needed).
- For PBIX files use Git LFS or attach PBIX to GitHub Releases.
