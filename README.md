# Mind Graph Hackathon

A hackathon project that **defuzzifies and deduplicates** student activity data from multiple sources (clubs, fests, organisers), builds **unified student profiles** and presents a **Streamlit** dashboard with analysis.

---

## What is data deduplication?

**Data deduplication** is the process of identifying and merging records that refer to the same real-world entity (e.g. the same person) even when they appear under slightly different names or in different datasets.

In this project:

- **Source data is “fuzzified”**: names and identifiers vary across files (typos, case, spacing, abbreviations).
- **We deduplicate by**:
  1. **Fuzzy name matching** — Using Python’s `difflib.SequenceMatcher`, we compare names from club events, fest participants, and organisers against a **ground-truth metadata** list (college-provided student names and IDs).
  2. **Threshold-based linking** — Names are corrected when similarity ratio exceeds a chosen threshold (e.g. 0.59–0.69 depending on the source).
  3. **Filtering invalid entries** — Dropping rows with very short or invalid names.
  4. **Merging into one view** — Combining club, fest, and organiser data into a single table keyed by **Roll No** from metadata, then building one **JSON profile per student** with all club/fest events and roles.

So the main motive is: **turn messy, duplicated, and inconsistent activity data into a single, clean set of student profiles** that can be validated against masked source data and used for analysis and product ideas.

---

## Project overview

- **Context**: Mind Graph Hackathon
- **Input**: Fuzzified CSVs (club events, fest participants, fest organisers) + college metadata (true names and IDs)
- **Output**:
  - **Unified profiles** in a pluggable JSON format (`profiles.json`)
  - **Analysis and visualisations** (e.g. in `notebooks/stats.ipynb`)
  - **Streamlit app** for market size, segmentation, demographics, and a SaaS consulting pitch

**TL;DR**

1. Build **unified student profiles** from the activity data (with deduplication as above).
   - Validation is against masked source data.
2. **Pitched a business solution** using the resulting analysis (e.g. analytics/consulting SaaS for organisers).

---

## Repository structure

```text
MindGraph-Hackathon/
├── README.md
├── Requirements.txt
├── app.py                 # Streamlit dashboard (run from repo root)
├── profiles.json          # Generated unified student profiles (output of main pipeline)
├── Datasets/              # Input CSVs
│   ├── Metadata.csv       # College source truth (Name, ID)
│   ├── Clubs_data.csv
│   ├── Organisers_In_Fests.csv
│   ├── Participants_In_Fests.csv
│   └── Combine.csv        # Combined/deduplicated data (from main pipeline)
├── Images/                # Charts and assets for Streamlit (roles, clubs, fests, etc.)
├── screenshots/           # Screenshots of the Streamlit app (for README)
└── notebooks/
    ├── main.ipynb         # Deduplication + profile-building pipeline
    ├── stats.ipynb        # Analysis and visualisations (e.g. Combine.csv)
    └── testing.ipynb      # Exploratory/testing on raw data
```

- **Notebooks** assume they are run with the repo root as the working directory (or paths are relative to `notebooks/`: e.g. `../Datasets/`, `../profiles.json`).
- **Streamlit** is intended to be run from the **repo root** so that `Images/` and `app.py` paths work as in `app.py`.

---

## Datasets

| File                                                         | Description                                             |
| ------------------------------------------------------------ | ------------------------------------------------------- |
| [Metadata.csv](Datasets/Metadata.csv)                           | College-provided source truth (student Name, ID).       |
| [Clubs_data.csv](Datasets/Clubs_data.csv)                       | All club events (club name, student name, event, role). |
| [Organisers_In_Fests.csv](Datasets/Organisers_In_Fests.csv)     | Fest organisers.                                        |
| [Participants_In_Fests.csv](Datasets/Participants_In_Fests.csv) | Participation list for fest events.                     |

**General info**: 3 clubs, 2 fests.

---

## How to run

1. **Clone the repo** and (optional) create a virtual environment:

   ```bash
   git clone <repo-url>
   cd MindGraph-Hackathon
   pip install -r Requirements.txt
   ```
2. **Regenerate profiles** (optional):Open `notebooks/main.ipynb`, run all cells. This reads from `../Datasets/`, deduplicates, and writes `../profiles.json` at the repo root.
3. **Run the Streamlit dashboard** from the **repo root**:

   ```bash
   streamlit run app.py
   ```

   Ensure the libraries in `Requirements.txt` are installed. The app expects an `Images/` folder with the chart assets (e.g. `roles.png`, `students.png`, `clubs.png`, `fest1.png`, `fest2.png`, `Club 1.png`, `Club 2.png`, `Club 3.png`). Add these if you have them locally.

   The app will open in your browser at `http://localhost:8501`.

---

## Capturing screenshots for the README

To add screenshots of the Streamlit app to this README:

1. **Start the Streamlit app** (from repo root):
   ```bash
   streamlit run app.py
   ```

2. **Open the app** in your browser at `http://localhost:8501`

3. **Take screenshots** of each section:
   - **Target Market** — Shows the 96% target market percentage
   - **Market Size** — Pie chart visualization (`roles.png`)
   - **Market Segmentation** — Two-column layout with student year distribution and clubs bar chart
   - **Demographics** — Student participation visualization
   - **Strengths and weaknesses** — Text analysis section
   - **Market Trends** — Fest participation charts (fest1.png, fest2.png) and club event analysis (Club 1-3.png)

4. **Save screenshots** to the `screenshots/` directory (already created)

5. **Add to README**: Once you have screenshots, you can add them using markdown image syntax:
   ```markdown
   ![Target Market](screenshots/target_market.png)
   ![Market Size](screenshots/market_size.png)
   ```

   **Tip**: On macOS, use `Cmd+Shift+4` to take selective screenshots, or use browser extensions like "Full Page Screen Capture" for full-page screenshots.

---

## Profile JSON format (pluggable)

Each student profile in `profiles.json` follows this structure:

```json
{
  "Name": "annette ahmed",
  "Id": "18XJ1A0100",
  "Clubs": {
    "club_1": {
      "isOrganiser": "organiser_1",
      "club_1_event_3": { "Participated": false }
    },
    "club_3": {
      "isOrganiser": "",
      "club_3_event_1": { "Participated": true }
    },
    "club_2": {
      "isOrganiser": "",
      "club_2_event_2": { "Participated": true }
    }
  },
  "Fests": {
    "fest_2": {
      "isOrganiser": "organiser_9",
      "fest_2_event_5": { "Participated": true }
    },
    "fest_1": {
      "isOrganiser": "organiser_9",
      "fest_1_event_5": { "Participated": true }
    }
  }
}
```

- **Name**, **Id**: from metadata after deduplication.
- **Clubs** / **Fests**: per club/fest, `isOrganiser` and per-event `Participated` (or organiser role).

---

## Tech stack & requirements

- **Streamlit** — dashboard and business pitch.
- **pandas** — data handling and merging.
- **Python stdlib** — `difflib.SequenceMatcher` for fuzzy matching.
- **matplotlib** — visualisations in notebooks.
- **Pillow** — image handling in Streamlit.
- **numpy** — used in notebooks.

See [Requirements.txt](Requirements.txt) for pinned versions.

---

## Mandatory hackathon requirements (reference)

1. **Streamlit** — used for the main app (`app.py`).
2. **Profile JSON** — submitted before presentation; produced by `notebooks/main.ipynb` as `profiles.json`.
3. **Pluggable format** — profile schema above is documented and consistent.

---

## Business idea (from the project)

From the analysed profiles, we proposed a **consulting/analytics SaaS** for event organisers: bridge the gap between clubs and participants using the deduplicated data and insights (e.g. market size ~96% of metadata, segmentation by year and club, event level participation). The Streamlit app presents target market, market size, segmentation, demographics, strengths/weaknesses and trends using the charts in `Images/`.

---

## License and attribution

Built for the Mind Graph hackathon back in 2022. Dataset and problem statement were given by the organisers.
